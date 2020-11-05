from flask_restful import Resource
from flask import g
from app import mongo_client
from utils.jwt_utils import verify_jwt
from bson.objectid import ObjectId

class UserChannelResource(Resource):

    def get(self):
        # 可登录可不登陆

        userid = g.userid
        conn = mongo_client.channel.info
        channel_list = []
        if userid:


            conn2 = mongo_client.person.user
            channelid_list = conn2.find_one({'_id':ObjectId(userid)},{'_id':0,'channels':1})['channels']
            print(channelid_list)

            for data in conn.find({'channelid':{'$in':channelid_list}},{'_id':0,'name':1,'channelid':1}):
                print(data)
                channel_list.append(data)

        else:
            for data in conn.find({},{'_id':0,'name':1,'channelid':1}):
                print(data)
                channel_list.append(data)

        return {'channels':channel_list}