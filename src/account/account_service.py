from db.dao.campaign_dao import CampaignDAO
from injector import inject
from db.dao.member_dao import MemberDAO
from entity.member import Member

class AccountService:
    @inject
    def __init__(self, member_dao: MemberDAO, campaign_dao: CampaignDAO):
        self._member_dao = member_dao
        self._campaign_dao = campaign_dao

    def join(self, member:Member) -> bool:
        result = self._member_dao.search_member(member.member_name)
        if not result is None:
            return False

        self._member_dao.insert_member(member)

        result = self._member_dao.search_member(member.member_name)
        if result is None:
            return False
        return True

    
    def get_data(self, member_name:str) -> Member:
        result = self._member_dao.search_member(member_name)
        return result