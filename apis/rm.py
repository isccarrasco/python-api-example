from flask_restplus import Namespace, Resource

api_rm = Namespace('RM Resources', description='Requirement Management')

@api_rm.route('/')
class RM(Resource):
    def get(self):
        # TO DO
        return 'GET RM'

    def post(self):
        # TO DO
        return 'POST RM'