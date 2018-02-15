# Workaround to make the project compatible both with Python 2 and Python 3
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup

from src.decorators import logger


@logger
def parse_announcements(url):
    """Extracts the announcements from the specified URL"""

    # Getting HTML content
    html_text = urlopen(url).read()

    # Processing it with BeautifulSoup
    soup = BeautifulSoup(html_text, "html.parser")

    # Getting all the announcements and adding them to an array
    html_announcements = soup.find_all('li')

    return html_announcements


def parse_announcement_title(url):

    # Getting HTML content
    html_text = urlopen(url).read()
    # Processing it with BeautifulSoup
    soup = BeautifulSoup(html_text, "html.parser")

    title = soup.find('span', class_='subject')

    return title.inner_html
