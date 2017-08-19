
class Announcement:
    """Announcement posted in the official KHUXNA site
    (currently, http://api.sp.kingdomhearts.com/information/list) """

    def __init__(self, id, title, link, date_posted):
        self.id = id
        self.title = title
        self.link = link
        self.date_posted = date_posted