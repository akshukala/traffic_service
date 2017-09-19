from flask import current_app as app
from flask import Flask
from flask.globals import request
from trafficservice.utils.resource import Resource
from nt_db.nt_db_app.models import *
from trafficservice.utils.auth import get_user 

class Cities(Resource):
    
    def get(self):
        term = request.args.get('term')
        if term:
            response = [{
                'city': str(city.city_name)
            }for city in City.objects.filter(is_active=True, city_name__istartswith=str(term))]
            return response
        else:
            city = []

        return list(set(city))
        
    #get.authenticated = False
    def post(self):
        try:
            request_data = request.get_json(force=True)
            City.objects.get_or_create(city_name=str(request_data['city_name']), created_by=get_user(), modified_by=get_user())
            return {"responseCode":200,
                    "Message":"""Success"""}
        except:
            return {"responseCode":400,
                    "Message":"""Something went wrong"""}
    