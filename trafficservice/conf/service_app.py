from nt_db.settings.pool import init_pool
from os.path import dirname, abspath

import django
from django.db import close_old_connections
from flask import Flask
from flask.ext import restful


from trafficservice.conf.config_logger_setup import setup_config_logger
from trafficservice.session.interfaces import DBInterface
from flask.ext.cors import CORS

from trafficservice.service_apis.ping import Ping
from trafficservice.service_apis.city import Cities
from trafficservice.service_apis.junction import Junctions

close_old_connections()
init_pool()

django.setup()
app = Flask(__name__)
CORS(app)
app.auth_header_name = 'X-Authorization-Token'
app.session_interface = DBInterface()
app.root_dir = dirname(dirname(abspath(__file__)))

api = restful.Api(app)

setup_config_logger(app)

app.logger.info("Setting up Resources")
api.add_resource(Ping,'/trafficservice/ping/')
api.add_resource(Cities, '/trafficservice/city/')
api.add_resource(Junctions,'/trafficservice/junction/')
app.logger.info("Resource setup done")

if __name__ == '__main__':
    # from gevent import monkey
    # from crmadminservice.utils.hacks import gevent_django_db_hack
    # gevent_django_db_hack()
    # monkey.patch_all(socket=True, dns=True, time=True, select=True, thread=False, os=True, ssl=True, httplib=False, aggressive=True)
    app.run(host="0.0.0.0", port=9862,threaded=True)
