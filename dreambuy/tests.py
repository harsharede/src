#!/usr/bin/python

import sqlite3, os
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_task_by_priority():
    resultdic = {}
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    database = BASE_DIR+"//db.sqlite3"
    print(database)
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT Product_id, Product_name, Product_bids,Product_Price FROM dreambuy_product")
    row = cur.fetchall()
    for i in row:
        resultdic[i[0]] = (i[2]/(i[3]/500))*100
    return resultdic

