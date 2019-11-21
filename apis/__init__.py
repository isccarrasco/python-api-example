from flask import Blueprint
from flask_restplus import Api

from .rm import api_rm as namespace_rm
from .qm import api_qm as namespace_qm

# Create Blueprint object with a common prefix
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint,
    title='PYTHON OSCL EXAMPLE',
    version='1.0',
    description='Implementation of Flask, Flask-RESTPlus, Blueprint, Namespaces.'
)

api.add_namespace(namespace_rm, path='/rm')
api.add_namespace(namespace_qm, path='/qm')