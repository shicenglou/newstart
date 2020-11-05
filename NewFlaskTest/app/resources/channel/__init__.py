from flask import Blueprint
from flask_restful import Api
from utils.contents import BASE_URL_PRIFIX
from utils.output import output_json
from .channels import AllChannels
from .article import ArticleListResource
# 创建蓝图对象

channel_bp = Blueprint('channel',__name__,url_prefix=BASE_URL_PRIFIX)

# 创建Api对象

channel_api = Api(channel_bp)

channel_api.representation('application/json')(output_json)

# 配置路由
channel_api.add_resource(AllChannels,'/channels')
channel_api.add_resource(ArticleListResource,'/articles')