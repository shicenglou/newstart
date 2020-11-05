from flask import Blueprint
from flask_restful import Api
from .passport import SMSCodeResource,LoginResource
from .profile import CurrentUserResource
from utils.contents import BASE_URL_PRIFIX
# 设置json包装格式
from utils.output import output_json
from .channel import UserChannelResource


# 1.创建蓝图对象
user_bp = Blueprint('user',__name__,url_prefix=BASE_URL_PRIFIX)

# 2.创建Api对象

user_api = Api(user_bp)
user_api.representation('application/json')(output_json)
# 3.添加类视图

user_api.add_resource(SMSCodeResource,'/sms/codes/<mob:mobile>')
user_api.add_resource(LoginResource,'/authorizations')
user_api.add_resource(CurrentUserResource,'/user')
user_api.add_resource(UserChannelResource,'/user/channels')