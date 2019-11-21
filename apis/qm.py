from flask_restplus import Namespace, Resource

api_qm = Namespace('QM Resources', description='Quality Management')

@api_qm.route('/')
class QM(Resource):
    def get(self):
        # TO DO 
        return 'GET QM'

    def post(self):
        # TO DO
        return 'POST QM'