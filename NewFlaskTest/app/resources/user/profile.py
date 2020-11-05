from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from utils.decorators import login_required
from flask import g
from app import mongo_client
from bson.objectid import ObjectId
class CurrentUserResource(Resource):
    # 传入装饰器
    method_decorators = {'get': [login_required]}

    def get(self):
        userid = g.userid
        print(userid)
        _id = ObjectId(userid)
        print(_id)
        db = mongo_client.person
        conn = db.user
        print('1')
        result = conn.find_one({'_id':_id})
        print(result)
        return {'name':result['name'],'age':result['age']}