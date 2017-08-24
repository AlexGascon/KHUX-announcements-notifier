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
