from flask import g
from functools import wraps

# 登陆验证装饰器
def login_required(f):

    @wraps(f)
    def wrapper(*args,**kwargs):
        if g.userid :
            return f(*args,**kwargs)
        else:
            return {'message': 'Invalid Token', 'data': None}, 401
    return wrapper