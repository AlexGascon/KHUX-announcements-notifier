import os
import pymongo

from src.constants import DB_COLLECTION_NAME, DB_NAME, DB_POSTED_KEY
from src.models import AnnouncementFactory


def get_database():
    """Connects to the DB and returns it"""
    connection = pymongo.MongoClient(os.environ.get("DB_CONNECTION_STRING"))
    db = connection[DB_NAME]

    return db


def get_collection():
    """Gets the collection we'll use to store the information and returns it"""
    db = get_database()
    collection = db[DB_COLLECTION_NAME]

    return collection


def insert_announcements(announcements):
    """Inserts the announcements into the database"""
    # TODO: Check if there's any way of reducing dependencies on this method.
    # Currently, it relies very heavily on the specific operation we want to
    # do and the structure of Announcement. This may change in the future
    # along with our requirements

    collection = get_collection()

    # If the announcement is new, we'll set its "posted" field to False
    update_content = {"$setOnInsert": {DB_POSTED_KEY: False}}
    for announcement in announcements:
        collection.update(announcement.to_mongo(), update_content, upsert=True)


def get_unposted_announcements():
    """Returns the Announcements objects that haven't been posted yet"""

    collection = get_collection()

    # Obtaining the MongoDB documents
    query = {DB_POSTED_KEY: False}
    unposted_documents = collection.find(query)

    # Converting them to Announcements
    unposted_announcements = []
    for document in unposted_documents:
        unposted_announcements.append(AnnouncementFactory.from_mongo(document))

    return unposted_announcements


def mark_announcement_as_posted(announcement):
    """Marks the specified announcement as posted"""

    collection = get_collection()

    find_query = {"_id": announcement.id}
    update_query = {"$set": {DB_POSTED_KEY: True}}

    collection.update_one(find_query, update_query)
