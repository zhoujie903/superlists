# superlists
学习《Test-Driven Development with Python》第2版的代码 [中文名：《Python Web开发：测试驱动方法》]

```shell
# 这个命令会创建一个名为 superlists 的文件夹
$ django-admin.py startproject superlists

$ tree superlists
superlists
├── manage.py
└── superlists
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

1 directory, 5 files

# 进入到superlists，执行如下命令，运行开发服务器
# 运行后，会生成db.sqlite3文件
$ python3 manage.py runserver

# 创建一个应用
$ python3 manage.py startapp lists

$ python3 manage.py startapp accounts

$ mkdir deploy_tools functional_tests
```
