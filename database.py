import psycopg2

# Establishing a connection to a postgres database
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='murei@123',dbname='myduka')

# Cur object
cur = conn.cursor()

cur.execute("select * from products")
products_table = cur.fetchall()
print(products_table)

cur.execute("select * from sales")
sales_table = cur.fetchall()
print(sales_table)