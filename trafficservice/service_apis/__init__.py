from trafficservice.utils.resource import Resource
class Ping(Resource):
    def get(self):
        return {"success":True}
