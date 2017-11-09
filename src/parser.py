# Workaround to make the project compatible both with Python 2 and Python 3
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup

from models import AnnouncementFactory
from src.decorators import logger

@logger
def parse_announcements(url):
    """Extracts the announcements from the specified URL"""

    # Getting HTML content
    html_text = urlopen(url).read()

    # Processing it with BeautifulSoup
    soup = BeautifulSoup(html_text, "html.parser")

    # Getting all the announcements and adding them to an array
    list_announcements = soup.find_all('li')
    announcements = []
    for html_announcement in list_announcements:
        announcement = AnnouncementFactory.announcement(html_announcement)
        # We'll only append it to the Announcements array if the string is ascii
        if announcement.is_ascii():
            announcements.append(announcement)

    return announcements
