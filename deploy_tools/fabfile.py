from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/zhoujie903/superlists.git'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    # _update_static_files(source_folder)
    # _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run(f'mkdir -p {site_folder}/{subfolder}')


def _get_latest_source(source_folder):

    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} && git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'cd {source_folder} && git reset --hard {current_commit}')

def _update_settings(source_folder, site_name):
    return
    settings_path = source_folder + '/superlists/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        f'ALLOWED_HOSTS = ["{site_name}"]'
    )
    secret_key_file = source_folder + '/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3.6 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')


# from fabric import Connection
# from invoke import task, run, env
#
# REPO_URL = 'https://github.com/zhoujie903/superlists.git'
#
# lc = Connection('parallels@10.211.55.3')
#
#
# @task(help={'name': "部署superlist"})
# def deploy(c):
#
#     site_folder = '/home/parallels/sites/www.superlist.com'
#     lc.run('mkdir -p {}'.format(site_folder))
#
#     with lc.cd(site_folder):
#         _get_latest_source()
#         _update_virtualenv()
#         _update_static_files()
#         _update_database()
#
#
# def _get_latest_source():
#     lc.run('git clone {} source'.format(REPO_URL))
#
#
# def _update_virtualenv():
#     lc.run('python3 -m virtualenv virtualenv')
#     lc.run('./virtualenv/bin/pip3 install -r source/requirements.txt')
#
#
# def _update_static_files():
#     lc.run('./virtualenv/bin/python3 source/manage.py collectstatic --noinput')
#
#
# def _update_database():
#     lc.run('mkdir -p database')
#     lc.run('./virtualenv/bin/python3 source/manage.py migrate --noinput')
#
#
# @task(help={'name': "Name of the person to say hi to."})
# def hello(c, name):
#     """
#     Say hi to someone.
#     """
#     print('hello Fabric! {}'.format(name))
#
#
#
