import unittest
from bs4 import BeautifulSoup

from src.models import AnnouncementFactory, Announcement
from src.parser import parse_announcement_title


class TestModels(unittest.TestCase):

    def setUp(self):
        self.title = "Test announcement title"
        self.id = "42"
        self.announcement = Announcement(title=self.title, announcement_id=self.id)
        self.mongoannouncement = {"title": self.title, "_id": self.id}

    def test_announcement_creation(self):
        """Testing if the fields have been correctly assigned"""
        assert self.announcement.id == self.id
        assert self.announcement.title == self.title

    def test_url(self):
        """Testing that the URL generates correctly"""
        url = "http://api.sp.kingdomhearts.com/information/detail/" + str(self.id)
        assert url == self.announcement.url

    def test_conversion_from_announcement_to_mongo(self):
        """Testing that the announcement converts adequately to its DB form"""
        assert self.announcement.to_mongo() == self.mongoannouncement

    def test_conversion_from_mongo_to_announcement(self):
        """Testing that the announcement is converted adequately from its DB form
        NOTE: we can't compare two objects with ==, so we'll compare its fields"""
        converted_announcement = AnnouncementFactory.from_mongo(self.mongoannouncement)
        assert converted_announcement.title == self.announcement.title
        assert converted_announcement.id == self.announcement.id

    def test_creation_from_announcementfactory(self):
        """Testing the creation of an announcement from its HTML content"""
        html_announcement = """
        <li>
        <span class="date">09/01</span><span class="news_cat cat2">UPDATE</span><a class="subject" href="detail/31606" target="_self">September Coliseum Update!</a>
        </li>
        """
        soup = BeautifulSoup(html_announcement, "html.parser")
        created_announcement = AnnouncementFactory.announcement(soup)
        assert created_announcement.title == "September Coliseum Update!"
        assert created_announcement.id == "31606"

    def test_reconverting_announcement(self):
        """Testing that we can convert to MongoDB form and back to Announcement"""
        reconverted_announcement = AnnouncementFactory.from_mongo(self.announcement.to_mongo())
        assert self.announcement.title == reconverted_announcement.title
        assert self.announcement.id == reconverted_announcement.id

    def test_reconverting_mongoannouncement(self):
        """Testing that we can convert to announcement and back to its MongoDB form"""
        reconverted_announcement = (AnnouncementFactory.from_mongo(self.mongoannouncement)).to_mongo()
        assert self.mongoannouncement["_id"] == reconverted_announcement["_id"]
        assert self.mongoannouncement["title"] == reconverted_announcement["title"]


class TestParser(unittest.TestCase):

    def test_parse_title(self):
        url = 'http://api.sp.kingdomhearts.com/information/detail/40171'
        self.assertEqual(parse_announcement_title(url), '0 AP Campaign!')


if __name__ == '__main__':
    unittest.main()
