import schedule
import time

from src.constants import ANNOUNCEMENT_URL
from src.db_utils import insert_announcements, get_unposted_announcements, mark_announcement_as_posted
from src.models import AnnouncementFactory
from src.parser import parse_announcements
from src.reddit import post_announcement
from src.decorators import logger


@logger
def parse_and_insert():
    # Insert announcements into DB
    url = ANNOUNCEMENT_URL
    html_announcements = parse_announcements(url)
    announcements = [AnnouncementFactory.announcement(html) for html in html_announcements]

    insert_announcements(announcements)


@logger
def initialize_notifier():
    """Parses all the announcements and marks them as posted
    Useful when starting the bot if it's been off for some time"""
    parse_and_insert()

    for announcement in get_unposted_announcements():
        mark_announcement_as_posted(announcement)


@logger
def execute_notifier():
    """Notifier. Parses the announcements and posts the new ones"""

    parse_and_insert()

    for announcement in get_unposted_announcements():
        post_announcement(announcement)
