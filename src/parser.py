import urllib2
from bs4 import BeautifulSoup

from models import AnnouncementFactory


def get_announcements(url):
    """Extracts the announcements from the specified URL"""

    # Getting HTML content
    html_text = urllib2.urlopen(url).read()

    # Processing it with BeautifulSoup
    soup = BeautifulSoup(html_text, "lxml")

    # Getting all the announcements and adding them to an array
    list_announcements = soup.find_all('li')
    announcements = []
    for html_announcement in list_announcements:
        announcement = AnnouncementFactory.announcement(html_announcement)
        announcements.append(announcement)

    return announcements
