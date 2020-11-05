from flask_restful import Resource
from app import mongo_client
from utils.decorators import login_required
from flask import g,request
from app import mongo_client
from bson.objectid import ObjectId
class AllChannels(Resource):
    method_decorators = {'put':[login_required]}
    def get(self):

        conn = mongo_client.channel.info
        channel_list = [data for data in conn.find({},{'_id':0,'name':1,'channelid':1})]
        return {'channels':channel_list}
    def put(self):
        #获取id
        userid = g.userid
        #获取更新后的channel id列表
        channels = request.json.get('channels')
        # 连接mongo，修改数据
        conn = mongo_client.person.user
        conn.update_one({'_id':ObjectId(userid)},{'$set':{'channels':channels}},upsert=True)
        # 修改完返回现在的频道
        channel_list = []
        conn2 = mongo_client.channel.info
        for num in channels:
            channel_list.append(conn2.find_one({'channelid':num},{'_id':0,'name':1,'channelid':1}))
        return {'channels':channel_list}
