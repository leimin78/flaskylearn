# flaskylearn
#使用git 进行代码管理
# 对目录进行重构
# 2017-04-12 目录结构如下
# 更新格式
FLASKY --- 文件夹
│  config.py  --- 配置文件
│  manage.py  --- 管理文件
│  requirements.txt --- 依赖包
│
└─app   --- 程序主目录
    │  models.py   --- 数据表，orm
    │  __init__.py
    │
    ├─main   --- 主入口
    │      errors.py --- 错误处理
    │      forms.py --- 表单处理
    │      views.py --- 视图逻辑处理
    │      __init__.py
    │
    ├─static --- 静态文件
    └─templates --- 模板文件