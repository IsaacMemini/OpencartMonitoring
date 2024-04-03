import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="opencart"
)


cur = conn.cursor()

def peopleOnline():
    conn.commit()
    cur.execute("SELECT COUNT(*) AS connected_customers FROM oc_session WHERE expire > NOW()")
    return cur.fetchone()

