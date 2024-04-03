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

def listOfBestSellingProducts():
    cur.execute("SELECT p.product_id, pd.name, SUM(op.quantity) AS total_quantity FROM oc_order_product op JOIN oc_product p ON op.product_id = p.product_id JOIN oc_product_description pd ON p.product_id = pd.product_id WHERE p.status = '1' GROUP BY p.product_id ORDER BY total_quantity DESC LIMIT 10")
    resultats = cur.fetchall()
    
