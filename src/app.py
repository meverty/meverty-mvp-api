from datetime import datetime
from dependency import configure
from entity.member import Member
from flask import Flask, jsonify, request, make_response
from flask_injector import FlaskInjector
from service.member_service import MemberService
from injector import inject

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    return jsonify(message='Meverty API v1 Server')


@inject
@app.route("/join", methods=['POST'])
def join(member_service:MemberService):
    params = request.get_json()
    member = Member(member_name=params['name'], join_date=datetime.now())
    result = member_service.join(member)
    return jsonify(message=result)


@inject
@app.route("/data/<member_name>")
def data(member_name, member_service:MemberService):
    result = member_service.get_data(member_name)
    if result is None:
        return jsonify(message='No Data')
    return jsonify(message={'id': result.id, 'member_name': result.member_name, 'join_date': result.join_date})


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Invalid Path'), 404)


FlaskInjector(app=app, modules=[configure])
