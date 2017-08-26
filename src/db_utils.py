import os
import pymongo

from src.constants import DB_COLLECTION_NAME, DB_NAME


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
    update_content = {"$setOnInsert": {"posted": False}}
    for announcement in announcements:
        collection.update(announcement.to_mongo(), update_content, upsert=True)

