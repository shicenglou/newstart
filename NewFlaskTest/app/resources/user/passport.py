from flask_restful import Resource
import random
from app import redis_client
from utils.contents import SMS_CODE_EXPIRE
from pymongo import MongoClient
from flask_restful.reqparse import RequestParser
from utils.jwt_utils import generate_jwt
from utils.parser import mobile as mobile_type
from datetime import datetime,timedelta
from flask import current_app
from flask_restful.inputs import regex
class SMSCodeResource(Resource):

    def get(self,mobile):
        rend_num = '%06d'%random.randint(0,999999)
        key = 'app:code:{}'.format(mobile)
        redis_client.set(key,rend_num,ex=SMS_CODE_EXPIRE)
        code = redis_client.get(key)
        print(key)
        print(code)
        data = {}
        data['mobile'] = mobile
        data['code'] = rend_num
        return data

class LoginResource(Resource):
    def __init__(self):
        client = MongoClient('127.0.0.1',27017)
        self.User = client.person
    def post(self):
        parser = RequestParser()
        parser.add_argument('mobile', required=True, location='json', type=mobile_type)
        parser.add_argument('code', required=True, location='json', type=regex(r'^\d{6}$'))
        args = parser.parse_args()
        mobile = args.mobile
        code = args.code
        # 验证验证码是否存在和正确:
        key = 'app:code:{}'.format(mobile)
        test_code = redis_client.get(key)
        print(mobile)
        print(code)
        print(key)
        print(test_code)
        if not test_code or test_code != code:
            return {'message':'Invalid Code','data':None}, 400
        # redis_client.delete(key)

        # 验证成功，从数据库查找用户
        conn = self.User.user
        result = conn.find_one({'mobile': mobile})
        if result is None or result == []:
            user_data = {'name':mobile,'mobile':mobile,'last_login':datetime.now(),'age':random.randint(15,35)}
            conn.insert_one(user_data)
            result = conn.find_one({'mobile':mobile})
        else:
            conn.update({'mobile': mobile}, {'$set': {'last_login': datetime.now()}}, upsert=True)
        print(result)

        # 生成token
        token = generate_jwt({'userid':str(result['_id'])},expiry=datetime.utcnow() + timedelta(days=current_app.config['JWT_EXPIRE_DAYS']))

        return {'token':token},201