import os

#获取当前文件的路径
basedir = os.path.abspath(os.path.dirname(__file__))

#定义配置文件,不同测试环境..delvelop, testing ..
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess secret key.'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.139.com'
    MAIL_PORT = 25
    MAIL_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass

class DelvelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flasky'



#注册delvelop 配置
config = {
    'delvelop' : DelvelopConfig
}