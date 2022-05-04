from entity.member import Member
from flask_restx import Namespace, Resource
from flask import request, jsonify
from injector import inject
from account.account_service import AccountService

Account = Namespace('Account')

@Account.route('/<string:member>')
class AccountData(Resource):
    @inject
    def __init__(self, account_service:AccountService, api):
        self._account_service = account_service
        super().__init__(api)

    def get(self, member):
        result = self._account_service.get_data(member)
        if result is None:
            return jsonify(message='No Data')
        return jsonify(message={
            'id': result.id, 
            'member_name': result.member_name, 
            'member_type': result.member_type,
            'join_timestamp': result.join_timestmap
        })

@Account.route("/join")
class AccountJoin(Resource):
    @inject
    def __init__(self, account_service:AccountService, api):
        self._account_service = account_service
        super().__init__(api)

    def post(self):
        params = request.get_json()
        member = Member(member_name=params['name'], member_type=params['type'])
        result = self._account_service.join(member)
        return jsonify(message=result)