from flask import request,g
from utils.jwt_utils import verify_jwt
 # 请求钩子函数 获取userid
def get_userinfo():
    token = request.headers.get('Authorization')

    g.userid = None

    if token:
        data = verify_jwt(token)
        if data:
            g.userid = data.get('userid')