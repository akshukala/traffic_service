import os
import time
from flask import current_app as app
from flask import Flask, redirect
from flask.globals import request
from trafficservice.utils.resource import Resource
from nt_db.nt_db_app.models import *
from trafficservice.utils.auth import get_user 

class Cities(Resource):
    
    def get(self):
        term = request.args.get('term')
        if term:
            city = City.objects.filter(is_active=True, city_name__istartswith=str(term)
                ).values_list('city_name')
        else:
            city = []

        return list(set(city))
    get.authenticated = False

    def post(self):
        try:
            City.objects.get_or_create(city_name=str(request.args.get('city_name')))
                                        # created_by=get_user(), modified_on=get_user())
            return {"responseCode":"200",
                    "Message":"""Success"""}
        except:
            return {"responseCode":"400",
                    "Message":"""Something went wrong"""}
    post.authenticated = False