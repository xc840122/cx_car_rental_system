"""
    @author: Peter
    @date: 16/08/2024
    @file: release_db.py
    @description: commit and release database connection
"""


def commit_and_close_connection(conn):
    """
    :param conn:
    :return:
    :description: method to commit and close the connection
    """
    conn.commit()
    conn.close()
