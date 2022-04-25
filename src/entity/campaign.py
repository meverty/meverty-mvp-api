from datetime import datetime


class Campaign:
    def __init__(self, campaign_name, member_name, id=0, impression=0, image_url="", setup_date=datetime.now()):
        self._id = id
        self._member_name = member_name
        self._setup_date = setup_date

        self.campaign_name = campaign_name
        self.impression = impression
        self.image_url = image_url
    
    
    @property
    def id(self):
        return self._id
    

    @property
    def campaingn_name(self):
        return self._campaign_name

    @campaingn_name.setter
    def campaign_name(self, value):
        self._campaign_name = value


    @property
    def member_name(self):
        return self._member_name


    @property
    def impression(self):
        return self._impression

    @impression.setter
    def impression(self, value):
        if value<0:
            raise ValueError("impression must be bigger than 0")
        self._impression = value


    @property
    def image_url(self):
        return self._image_url
    
    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    

    @property
    def setup_date(self):
        return self._setup_date