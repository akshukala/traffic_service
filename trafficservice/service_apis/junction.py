import os
import time
from flask import current_app as app
from flask import Flask, redirect
from flask.globals import request
from flask_restful import Resource
from trafficservice.utils.resource import Resource
from nt_db.nt_db_app.models import *
from trafficservice.utils.auth import get_user 

class Junctions(Resource):
    
    def get(self):
        if int(request.args.get('type')) == 1:
            print request.args.get('city')
            return [{
                    "junction_id":junction.id,
                    "junction_name":str(junction.junction_name)
                    }
                    for junction in Junction.objects.filter(city__city_name =request.args.get('city'), is_active=True)]
        else:
            return [{
                    "junction_id":junction.id,
                    "junction_name":str(junction.junction.junction_name),
                    "hour": junction.hour,
                    "minute" : junction.minute,
                    "second": junction.second,
                    "day": junction.day,
                    "month":junction.month,
                    "year":junction.year,
                    "phase_no":junction.phase_no,
                    "status":junction.status,
                    "normal_time":junction.normal_time,
                    "step_elased_time":junction.step_elased_time,
                    "cycle_elased_time1":junction.cycle_elased_time1,
                    "cycle_elased_time2":junction.cycle_elased_time2,
                    "working_on":junction.working_on,
                    "mode":junction.mode,
                    "pahse1":junction.phase1,
                    "pahse2":junction.phase2,
                    "pahse3":junction.phase3,
                    "pahse4":junction.phase4,
                    "pahse5":junction.phase5,
                    "pahse6":junction.phase6,
                    "pahse7":junction.phase7,
                    "pahse8":junction.phase8,
                    "total_cycle_time1":junction.total_cycle_time1,
                    "total_cycle_time2":junction.total_cycle_time2
                    }
                    for junction in Junction_data.objects.filter(junction=int(request.args.get('id')))]



    def post(self):
        request_data = request.get_json(force=True)
        try:
            Junction.objects.get_or_create(junction_name=str(request_data['junction_name']),
                                        city = City.objects.get(city_name=str(request_data['city'])),
                                        road_name1 = str(request_data['road_name1']),
                                        road_name2 = str(request_data['road_name2']),
                                        road_name3 = str(request_data['road_name3']),
                                        road_name4 = str(request_data['road_name4']),
                                        road_name5 = str(request_data['road_name5']),
                                        road_name6 = str(request_data['road_name6']),
                                        road_name7 = str(request_data['road_name7']),
                                        road_name8 = str(request_data['road_name8']),
                                        created_by=get_user(), modified_by=get_user(),
                                        is_active = True)

            # Junction.objects.create(junction_name=str(request.form['junction_name']),
            #                             city = City.objects.get(id=int(request_data['city'])),
            #                             hour = int(request.form['hour']),
            #                             minute = int(request.form['minute']),
            #                             second = int(request.form['second']),
            #                             day = int(request.form['day']),
            #                             month = int(request.form['month']),
            #                             year = int(request.form['year']),
            #                             phase_no = int(request.form['phase_no']),
            #                             status = int(request.form['status']),
            #                             normal_time = int(request.form['normal_time']),
            #                             step_elased_time = int(request.form['step_elased_time']),
            #                             cycle_elased_time1 = int(request.form['cycle_elased_time1']),
            #                             cycle_elased_time2 = int(request.form['cycle_elased_time2']),
            #                             working_on = int(request.form['working_on']),
            #                             total_cycle_time1 = int(request.form['total_cycle_time1']),
            #                             total_cycle_time2 = int(request.form['total_cycle_time2']),
            #                             mode = int(request.form['mode']),
            #                             is_active = True)
            return {"responseCode":200,
                    "Message":"""Success"""}
        except:
            return {"responseCode":400,
                    "Message":"""Something went wrong"""}