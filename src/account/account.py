from entity.member import Member
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from injector import inject
from account.account_service import AccountService

Account = Namespace('Account')

@Account.route('/<string:member>')
class AccountData(Resource):
    
    join_model = Account.model('Member', {  # Model 객체 생성
        'member_type': fields.String(description='member type', required=True, example="Advertiser")
    })

    @inject
    def __init__(self, account_service:AccountService, api):
        self._account_service = account_service
        super().__init__(api)

    @Account.doc(params={'member': '사용자 이름'})
    def get(self, member):
        """기존 사용자의 정보를 가져옵니다."""
        result = self._account_service.get_data(member)
        if result is None:
            return jsonify(message='No Data')
        
        return jsonify({
            'id': result.id, 
            'member_name': result.member_name, 
            'member_type': result.member_type,
            'join_timestamp': result.join_timestmap
        })
        
    @Account.expect(join_model)
    @Account.doc(params={'member': '사용자 이름'})
    def post(self, member):
        """새로운 사용자를 추가합니다."""
        params = request.get_json()
        member = Member(member_name=member, member_type=params['member_type'])
        result = self._account_service.join(member)
        return jsonify({'result': result})