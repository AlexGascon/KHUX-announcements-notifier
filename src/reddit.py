import os

import praw

from src.constants import BOT_USER_AGENT, BOT_USERNAME
from src.db_utils import mark_announcement_as_posted
from src.decorators import logger

@logger
def get_subreddit():
    """Returns an instance of the subreddit we'll post to"""

    # Obtaining a Reddit instance and pointing it to the subreddit
    reddit = praw.Reddit(user_agent=BOT_USER_AGENT,
                         client_id=os.environ.get("CLIENT_ID"),
                         client_secret=os.environ.get("CLIENT_SECRET"),
                         username=BOT_USERNAME,
                         password=os.environ.get("BOT_PASSWORD"))
    subreddit = reddit.subreddit(os.environ.get("SUBREDDIT"))
    return subreddit

@logger
def post_announcement(announcement):
    """Posts an Announcement to the default subreddit"""

    # Getting the subreddit
    subreddit = get_subreddit()

    # Preparing the submission
    title = "[KHUX] {title}".format(title=announcement.title)
    url = announcement.url

    # Submitting
    try:
        submission = subreddit.submit(title=title, url=url)
        mark_announcement_as_posted(announcement)
        print("Posted announcement {}".format(announcement))

        return submission

    except praw.exceptions.APIException as e:
        print ("API Rate Limit error: " + e.message)

        # In the first stages of the bot, we will simply ignore the unposted announcements.
        # Posting them later could be unnecessary spam.
        # TODO: Change in future releases
        mark_announcement_as_posted(announcement)

        return None

