# 路由转换器
import re
from werkzeug.routing import BaseConverter
class MobileConverter(BaseConverter):
    # 手机号格式
    regex = r'1[3-9]\d{9}'

def register_converter(app):
    app.url_map.converters['mob'] = MobileConverter