import psycopg2
import settings

POSTGRESQL_PASSWORD = settings.POSTGRESQL_PASSWORD


def connect():
    con = psycopg2.connect(
        "host=" +
        "ec2-3-226-134-153.compute-1.amazonaws.com" +
        " port=" +
        "5432" +
        " dbname=" +
        "dattf8etr7boo2" +
        " user=" +
        "zjgshrfbwpudpr" +
        " password=" +
        POSTGRESQL_PASSWORD)

    return con


def select_execute(con, sql):
    with con.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    return rows


def insert_execute(con, sql):
    with con.cursor() as cur:
        cur.execute(sql)
    con.commit()
