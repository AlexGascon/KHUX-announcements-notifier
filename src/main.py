import schedule
import time

from src.constants import ANNOUNCEMENT_URL
from src.db_utils import insert_announcements, get_unposted_announcements, mark_announcement_as_posted
from src.parser import parse_announcements
from src.reddit import post_announcement
from src.decorators import logger

@logger
def parse_and_insert():
    # Insert announcements into DB
    url = ANNOUNCEMENT_URL
    announcements = parse_announcements(url)
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

    announcements_to_post = get_unposted_announcements()
    if announcements_to_post:
        for announcement in announcements_to_post:
            post_announcement(announcement)


# Setting the task to run periodically
# ABOUT: The announcements get posted (generally) at 9:00 AM GMT+2 time. As schedule (or the Heroku server) uses
# UTC time, this translates to 7:00 AM UTC
schedule.every().day.at("7:00").do(execute_notifier)

# Setting all announcements to posted on init
initialize_notifier()

while True:
    schedule.run_pending()
    time.sleep(60)
