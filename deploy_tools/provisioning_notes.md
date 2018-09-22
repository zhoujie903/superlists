配 置 新 网 站 
=========

## 需 要 安 装 的 包： 

* nginx 
* Python 3 
* Git 
* pip 
* virtualenv 

以 Ubuntu 为 例， 可 以 执 行 下 面 的 命 令 安 装：

sudo apt-get install nginx git python3 python3-pip

sudo pip3 install virtualenv 

## 配 置 Nginx 虚 拟 主 机 

* 参 考 nginx.template.conf 
* 把 SITENAME 替 换 成 所 需 的 域 名， 例 如 staging.my-domain.com 

## Upstart 任 务 

* 参 考 gunicorn-upstart.template.conf 
* 把 SITENAME 替 换 成 所 需 的 域 名， 例 如 staging.my-domain.com 

## 文 件 夹 结 构： 

假 设 有 用 户 账 户， 家 目 录 为/home/username

```
/home/username 
    └ ─ ─ sites
        └ ─ ─ SITENAME 
            ├ ─ ─ database 
            ├ ─ ─ source 
            ├ ─ ─ static 
            └ ─ ─ virtualenv
```


