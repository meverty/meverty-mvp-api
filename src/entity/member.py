class Member:
    def __init__(self, member_name, join_date, id=0):
        self.id = id
        self.member_name = member_name
        self.join_date = join_date
    
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
    def join_date(self):
        return self._join_date

    @join_date.setter
    def join_date(self, value):
        self._join_date = value