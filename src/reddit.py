import os

import praw

from constants import BOT_USER_AGENT, BOT_USERNAME, SUBREDDIT_TO_USE


def get_subreddit():
    """Returns an instance of the subreddit we'll post to"""

    # Obtaining a Reddit instance and pointing it to the subreddit
    reddit = praw.Reddit(user_agent=BOT_USER_AGENT,
                         client_id=os.environ.get("CLIENT_ID"),
                         client_secret=os.environ.get("CLIENT_SECRET"),
                         username=BOT_USERNAME,
                         password=os.environ.get("BOT_PASSWORD"))
    subreddit = reddit.subreddit(SUBREDDIT_TO_USE)
    return subreddit


def post_announcement(announcement):
    """Posts an Announcement to the default subreddit"""

    # Getting the subreddit
    subreddit = get_subreddit()

    # Preparing the submission
    title = "[KHUX] {title}".format(title=announcement.title)
    url = announcement.url

    # Submitting
    submission = subreddit.submit(title=title, url=url)

    return submission
