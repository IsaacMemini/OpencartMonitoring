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

def customerRetentionRate():
    conn.commit()
    cur.execute("SELECT (COUNT(DISTINCT order_id_recurrent) / COUNT(DISTINCT order_id)) * 100 AS taux_retour_client FROM    (SELECT   o1.customer_id,            o1.order_id AS order_id_recurrent,MIN(o2.order_id) AS order_id FROM oc_order o1 LEFT JOIN oc_order o2 ON o1.customer_id = o2.customer_id AND o1.order_id < o2.order_id    GROUP BY o1.order_id) AS recurrent_orders")
    return int(cur.fetchone()[0])


    
def revenue():
    conn.commit()
    cur.execute("SELECT SUM(total) AS total_revenue FROM oc_order WHERE order_status_id IN (1, 5, 7)")
    return int(cur.fetchone()[0])

def numberOfConversion():
    conn.commit()
    cur.execute("SELECT COUNT(*) AS total_conversions FROM oc_order WHERE order_status_id = 1")
    return cur.fetchone()

def abandonedCart():
    conn.commit()
    cur.execute("SELECT COUNT(*) AS abandoned_carts FROM oc_cart WHERE customer_id = 0 AND date_added > DATE_SUB(NOW(), INTERVAL 1 DAY)")
    return cur.fetchone()

def activeShoppingSession():
    conn.commit()
    cur.execute("SELECT COUNT(DISTINCT session_id) AS active_shopping_sessions FROM oc_cart WHERE date_added > DATE_SUB(NOW(), INTERVAL 24 HOUR)")
    return cur.fetchone()

