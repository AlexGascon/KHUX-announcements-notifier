
class Announcement:
    """Announcement posted in the official KHUXNA site
    (currently, http://api.sp.kingdomhearts.com/information/list) """

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return "Announcement(id={id}, title={title})".format(id=self.id,
                                                             title=self.title)

    def __str__(self):
        return "Announcement: {title}".format(title=self.title)
