from flask_restful import Resource
from app import mongo_client
from utils.contents import HOME_PRE_PAGE
from flask_restful.reqparse import RequestParser
from datetime import datetime
from time import time
class ArticleListResource(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('channel_id',location='args',required=True,type=int)
        parser.add_argument('timestamp',location='args',required=True,type=int)
        args = parser.parse_args()
        channel_id = args.channel_id
        timestamp = args.timestamp
        # 推荐为空，返回空

        if channel_id == 0:
            return {'result':[],'pre_timestamp':0}
        date = datetime.fromtimestamp(timestamp*0.001)
        date1 = time()
        date2 = datetime.fromtimestamp(date1)
        print(date)
        print(date1)
        print(date2)
        print('..............................')
        return {}