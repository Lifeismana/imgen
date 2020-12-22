import json
import secrets
import os

test_config = None
try:
    test_config = json.load(open("config/config.json"))
except FileNotFoundError:
    test_config = {}
    if not os.path.exists('config'):
        os.mkdir('config')
    elif not os.path.isdir('config'):
        raise Exception("config is not a folder")

test = os.getenv("IMGEN_SECRET_KEY",test_config.get("client_secret"))

if test is None:
    test_config['client_secret'] = secrets.token_urlsafe(24)

with open('config/config.json', 'w') as outfile:
    json.dump(test_config, outfile)

bind= os.getenv("IMGEN_HOSTNAME",test_config.get("hostname",'127.0.0.1'))+':'+str(os.getenv("IMGEN_PORT",test_config.get('port',65535)))
workers = os.getenv("IMGEN_NUM_WORKERS",test_config.get("num_workers",1))
worker_class = 'gevent'



