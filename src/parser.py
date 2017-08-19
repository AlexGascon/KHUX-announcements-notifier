import urllib2
from bs4 import BeautifulSoup

from models import Announcement


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
        announcement = process_anouncement(html_announcement)
        announcements.append(announcement)

    return announcements


def process_anouncement(html_announcement):
    """Creates an Announcement object given its HTML content"""

    title = html_announcement.a.text
    # The href has the form "detail/<id_number>". We just want the number
    href = html_announcement.a['href']
    id = href.split("/")[1]

    return Announcement(title=title, id=id)