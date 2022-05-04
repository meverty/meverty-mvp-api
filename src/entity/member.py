from datetime import datetime

class Member:
    def __init__(self, member_name, member_type, id=0, join_timestamp=datetime.now()):
        self.id = id
        self.member_name = member_name
        self.join_timestmap = join_timestamp
        self.member_type = member_type
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id=value

    
    @property
    def member_name(self):
        return self._member_name
    
    @member_name.setter
    def member_name(self, value):
        self._member_name = value


    @property
    def join_timestmap(self):
        return self._join_timestmap

    @join_timestmap.setter
    def join_timestmap(self, value):
        self._join_timestmap = value

    
    @property
    def member_type(self):
        return self._member_type
    
    @member_type.setter
    def member_type(self, value):
        self._member_type = value
