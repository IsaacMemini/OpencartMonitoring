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

def totalCustomers():
    conn.commit()
    cur.execute("SELECT COUNT(*) AS TotalCustomers FROM oc_customer")
    return cur.fetchone()

def totalSales():
    conn.commit()
    cur.execute("SELECT sum(value) AS TotalSales FROM oc_order_total where code = 'total'")
    return int(cur.fetchone()[0])

