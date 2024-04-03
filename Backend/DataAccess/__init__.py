from contextlib import contextmanager
import pymssql
import traceback
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MSSQL_SERVER = getenv("MSSQL_SERVER")
MSSQL_DATABASE = getenv("MSSQL_DATABASE")
MSSQL_PORT = getenv("MSSQL_PORT")

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=6))
@contextmanager
def get_database(as_dict=True):
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
