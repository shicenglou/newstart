class DefaultConfig:
    """默认配置"""
    # redis配置
    REDIS_HOST = '127.0.0.1'  # ip
    REDIS_PORT = 6379  # 端口
    JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'  # 秘钥
    JWT_EXPIRE_DAYS = 14  # JWT过期时间
    MONGO_PORT = 27017
    pass


config_dict = {
    'dev': DefaultConfig
}