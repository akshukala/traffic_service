import os
import time
from flask import current_app as app
from flask import Flask, redirect
from flask.globals import request
from flask_restful import Resource
from trafficservice.utils.resource import Resource
from nt_db.nt_db_app.models import *

class Junctions(Resource):
    
    def get(self):
        term = request.args.get('term')
        if term:
            junctions = Junction.objects.filter(is_active=True, junction_name__istartswith=str(term)
                ).values_list('junction_name')
        else:
            junctions = []

        return list(set(junctions))
    get.authenticated = False


    def post(self):
        import pdb
        pdb.set_trace()
        try:
            City.objects.get_or_create(city_name=str(request.form['city_name']))
            return {"responseCode":"200",
                    "Message":"""Success"""}
        except:
            return {"responseCode":"400",
                    "Message":"""Something went wrong"""}
    get.authenticated = False