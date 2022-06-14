from account.account import Account
from advertisement.advertisement import Advertisement
from metaverse.metaverse import Metaverse
from dependency import configure
from flask import Flask, jsonify, request, make_response
from flask_injector import FlaskInjector
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

api = Api(app, version='1.0', title='Meverty API', description='API description for Meverty Service')

api.add_namespace(Metaverse, '/metaverse')
api.add_namespace(Account, '/account')
api.add_namespace(Advertisement, '/advertisement')


FlaskInjector(app=app, modules=[configure])
