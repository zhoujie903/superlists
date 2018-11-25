[TOC]
# superlists
学习《Test-Driven Development with Python》第2版的代码 [中文名：《Python Web开发：测试驱动方法》]

## 文件夹和文件的由来
```shell
# 1. superlists文件夹
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

# 2. lists、accounts文件夹
# 创建一个应用
$ python3 manage.py startapp lists

$ python3 manage.py startapp accounts

# 3. deploy_tools、functional_tests文件夹
$ mkdir deploy_tools functional_tests
```

## 部署

远程部署：
比如“服务器”为：parallels@10.211.55.3[Ubuntu 16.0.4]
本机：macOS,已安装Fabric,已安装Ansible

**deploy_tools/fabfile.py还是Fabric1.x版本**
Fabric使用的还是1.x版本
```
➜  ~ pip3 list
Package            Version
------------------ ----------
Fabric3            1.14.post1
```

1. 下载deploy_tools目录到本机
2. 本机运行deploy_tools/fabfile.py
```
cd deploy_tools 
fab -u parallels -H 10.211.55.3 deploy
# 在服务器上会生成~/sites/10.211.55.3目录  
```
3. 本机运行deploy_tools/provision.ansible.yaml
```
ansible-playbook -i inventory.ansible provision.ansible.yaml -K
# -K, --ask-become-pass ask for privilege escalation password  
```


