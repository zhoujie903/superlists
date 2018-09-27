from fabric import Connection
from invoke import task, run, env

REPO_URL = 'https://github.com/zhoujie903/superlists.git'

lc = Connection('parallels@10.211.55.3')


@task(help={'name': "部署superlist"})
def deploy(c):

    site_folder = '/home/parallels/sites/www.superlist.com'
    lc.run('mkdir -p {}'.format(site_folder))

    with lc.cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _update_static_files()
        _update_database()


def _get_latest_source():
    lc.run('git clone {} source'.format(REPO_URL))


def _update_virtualenv():
    lc.run('python3 -m virtualenv virtualenv')
    lc.run('./virtualenv/bin/pip3 install -r source/requirements.txt')


def _update_static_files():
    lc.run('./virtualenv/bin/python3 source/manage.py collectstatic --noinput')


def _update_database():
    lc.run('mkdir -p database')
    lc.run('./virtualenv/bin/python3 source/manage.py migrate --noinput')


@task(help={'name': "Name of the person to say hi to."})
def hello(c, name):
    """
    Say hi to someone.
    """
    print('hello Fabric! {}'.format(name))



