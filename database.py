import psycopg2

# Establishing a connection to a postgres database
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='murei@123',dbname='myduka')

# Cur object
cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data

# Method 1
# Susceptible to sql injection:

def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

product1=('shoes',2500,3000)
product2=('phone',10000,17000)
product3=('biscuits',150,360)
product4=('flour',2500,4000)
product5=('rice',4500,6200)

# insert_products(product1)
# insert_products(product2)
# insert_products(product3)
# insert_products(product4)
# insert_products(product5)

products_data=get_products()
print(products_data)

# Method 2
# Not susceptible to sql injection, hence more secure:

def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

product6=('laptop',50000,75000)
# insert_products2(product6)

print(products_data)

# NB: %s is a placeholder

# Task 1.Using functions write code to: 
# -> get_stock() 

def get_stocks():
    cur.execute("select * from stock")
    stocks_data = cur.fetchall()
    return stocks_data

stocks_data = get_stocks()
print(stocks_data)

# -> insert sales() 

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()

sales1=(1,5)
sales2=(2,7)
sales3=(3,23)


# insert_sales(sales1)
# insert_sales(sales2)
# insert_sales(sales3)


sales_data=get_sales()
print(sales_data)

# -> insert_stock()
def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",values)
    conn.commit()

stock1=(1,27)
stock2=(2,35)
stock3=(3,56)

# insert_stock(stock1)
# insert_stock(stock2)
# insert_stock(stock3)

stocks_data = get_stocks()
print(stocks_data)

def sales_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date, SUM(sales.quantity * products.selling_price) 
        AS sales_per_day FROM sales JOIN products ON sales.pid = products.id 
        GROUP BY DATE(created_at) ORDER BY sale_date; 

""")
    daily_sales=cur.fetchall()
    return daily_sales

def profit_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date, 
        SUM((products.selling_price - products.buying_price) * sales.quantity) 
        AS profit_per_day FROM sales JOIN products ON sales.pid = products.id 
        GROUP BY DATE(created_at) ORDER BY sale_date;
""")
    daily_profit=cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
        SELECT name, SUM(sales.quantity) AS sales_per_product FROM sales
        JOIN products ON sales.pid = products.id GROUP BY name;
""")
    product_sales=cur.fetchall()
    return product_sales

def profit_per_product():
    cur.execute("""
        SELECT name, SUM((products.selling_price - products.buying_price) * sales.quantity) 
        AS profit_per_product FROM sales JOIN products ON sales.pid = products.id GROUP BY name;
""")
    product_profit=cur.fetchall()
    return product_profit

def  check_available_stock(pid):
    cur.execute("select sum(stock.stock_quantity) from stock where pid = %s",(pid,))
    total_stock = cur.fetchone() [0] or 0 # [0] extracts the first value of the tuple fetchone()

    cur.execute("select sum(sales.quantity) from sales where pid = %s",(pid,))
    total_sold = cur.fetchone() [0] or 0

    return total_stock - total_sold

def check_user_exists(email):
    cur.execute("select * from user where email = %s"(email,))
    user = cur.fetchone()
    return user

def create_user(user_details):
    cur.execute("insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)",user_details)
    conn.commit()

    # user_details is already a tuple, hence no comma after it on cur.execute()