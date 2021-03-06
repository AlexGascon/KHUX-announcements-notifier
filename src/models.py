from src.constants import BASE_URL
from src.parser import parse_announcement_title


class Announcement:
    """Announcement posted in the official KHUXNA site
    (currently, http://api.sp.kingdomhearts.com/information/list) """

    def __init__(self, announcement_id, title):
        self.id = announcement_id
        self.title = title

    def __repr__(self):
        return "Announcement(announcement_id={id}, title={title})".format(id=self.id,
                                                                          title=self.title)

    def __str__(self):
        return "Announcement: {title}".format(title=self.title)

    @property
    def url(self):
        """Returns the URL of the announcement

        The URLs are of the form http://api.sp.kingdomhearts.com/information/detail/<id>"""
        base_url = BASE_URL
        return base_url + "information/detail/{id}".format(id=self.id)

    def is_ascii(self):
        """Checks if all the chars in the announcement are ASCII"""
        return all(ord(char) < 128 for char in self.title)

    def to_mongo(self):
        """Converts the announcement into a format suitable for MongoDB (a dict)

        The explicit conversion of title to str is to avoid getting strings of
        type Unicode, as they throw errors when inserted into MongoDB"""
        return {"_id": self.id, "title": str(self.title)}


class AnnouncementFactory:
    """Wrapper to create an Announcement object from HTML code.

    This lets us have a better control over the fields used or the way
    they are processed to create instances
    """

    @classmethod
    def announcement(cls, html_announcement):
        """Creates an Announcement object given its HTML content"""

        # The href has the form "detail/<id_number>". We just want the number
        href = html_announcement.a['href']
        announcement_id = href.split("/")[1]

        announcement = Announcement(title="", announcement_id=announcement_id)
        title = parse_announcement_title(announcement.url)
        announcement.title = title

        return announcement

    @classmethod
    def from_mongo(cls, mongo_announcement):
        """Creates an Announcement object given its MongoDB form"""
        return Announcement(title=mongo_announcement["title"],
                            announcement_id=mongo_announcement["_id"])
