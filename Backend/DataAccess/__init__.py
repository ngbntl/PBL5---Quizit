from contextlib import contextmanager
from os.path import dirname, join, normpath

import pymssql
import traceback
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from dotenv import load_dotenv
from os import getenv

import secrets
from string import ascii_letters, digits


def generate_id(n: int) -> str:
    return ''.join(secrets.choice(ascii_letters + digits) for _ in range(n))


# MSSQL_SERVER
dotenv_path = normpath(join(dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path)
MSSQL_SERVER = getenv("MSSQL_SERVER")
MSSQL_DATABASE = getenv("MSSQL_DATABASE")
MSSQL_PORT = getenv("MSSQL_PORT")


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=6))
@contextmanager
def get_MS_database(as_dict=True):
    mssql_connection = pymssql.connect(server=MSSQL_SERVER, database=MSSQL_DATABASE, port=MSSQL_PORT, as_dict=as_dict)
    cursor = mssql_connection.cursor()

    try:
        yield cursor
        mssql_connection.commit()
    except pymssql.Error as e:
        logging.error(f"Database error occurred: {e}")
        traceback.print_exc()
        mssql_connection.rollback()
        raise e
    finally:
        mssql_connection.close()


# MONGODB
from pymongo import MongoClient

MONGODB_SERVER = getenv("MONGODB_SERVER")
MONGODB_DATABASE = getenv("MONGODB_DATABASE")


@contextmanager
def get_mongodb_database():
    client = MongoClient(MONGODB_SERVER)
    db = client[MONGODB_DATABASE]

    try:
        yield db
    finally:
        client.close()
