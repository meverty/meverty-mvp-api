from datetime import datetime


class Campaign:
    def __init__(self, campaign_name, member_id, campaign_type, interaction_url, 
                    id=0, image_url="https://d19748wxcujmgp.cloudfront.net/default.png", setup_date=datetime.now(), activated = True):
        self._id = id
        self._member_id = member_id
        self._setup_date = setup_date

        self.campaign_name = campaign_name
        self.image_url = image_url
        self.campaign_type = campaign_type
        self.interaction_url = interaction_url
        self.activated = activated
    
    @property
    def id(self):
        return self._id

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, value):
        self._campaign_name = value

    @property
    def member_id(self):
        return self._member_id

    @property
    def image_url(self):
        return self._image_url
    
    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    

    @property
    def setup_date(self):
        return self._setup_date

    @property
    def campaign_type(self):
        return self._campaign_type
    
    @campaign_type.setter
    def campaign_type(self, value):
        self._campaign_type = value


    @property
    def interaction_url(self):
        return self._interaction_url
    
    @interaction_url.setter
    def interaction_url(self, value):
        self._interaction_url = value

    @property
    def activated(self):
        return self._activated

    @activated.setter
    def activated(self, value):
        self._activated = value
