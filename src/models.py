from constants import BASE_URL


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

    @property
    def url(self):
        """Returns the URL of the announcement

        The URLs are of the form http://api.sp.kingdomhearts.com/information/detail/<id>"""
        base_url = BASE_URL
        return BASE_URL + "information/detail/{id}".format(id=self.id)




class AnnouncementFactory:
    """Wrapper to create an Announcement object from HTML code.

    This lets us have a better control over the fields used or the way
    they are processed to create instances
    """

    @classmethod
    def announcement(cls, html_announcement):
        """Creates an Announcement object given its HTML content"""

        title = html_announcement.a.text
        # The href has the form "detail/<id_number>". We just want the number
        href = html_announcement.a['href']
        announcement_id = href.split("/")[1]

        return Announcement(title=title, id=announcement_id)
