import schedule
import time

from src.constants import ANNOUNCEMENT_URL
from src.db_utils import insert_announcements, get_unposted_announcements, mark_announcement_as_posted
from src.parser import parse_announcements
from src.reddit import post_announcement

def parse_and_insert():
    # Insert announcements into DB
    url = ANNOUNCEMENT_URL
    announcements = parse_announcements(url)
    insert_announcements(announcements)

def initialize_notifier():
    """Parses all the announcements and marks them as posted
    Useful when starting the bot if it's been off for some time"""
    parse_and_insert()

    for announcement in get_unposted_announcements():
        mark_announcement_as_posted(announcement)

def execute_notifier():
    """Notifier. Parses the announcements and posts the new ones"""
    print("Running execute_notifier")

    parse_and_insert()

    announcements_to_post = get_unposted_announcements()
    if announcements_to_post:
        for announcement in announcements_to_post:
            post_announcement(announcement)

    print("Ending execute_notifier")

    
schedule.every().day.at("9:00").do(execute_notifier())

while True:
    schedule.run_pending()
    time.sleep(600)
