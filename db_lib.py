import psycopg2
import settings

POSTGRESQL_PASSWORD = settings.POSTGRESQL_PASSWORD


def connect():
    con = psycopg2.connect(
        "host=" +
        "ec2-3-234-22-132.compute-1.amazonaws.com" +
        " port=" +
        "5432" +
        " dbname=" +
        "d5dbc2jvq1qgrt" +
        " user=" +
        "gyhpuwaqxnuskp" +
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
