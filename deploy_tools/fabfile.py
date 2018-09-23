import fabric
import random

REPO_URL = "https://github.com/zhoujie903/superlists.git"

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'