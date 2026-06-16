from flask import Flask, render_template,request,redirect,url_for
from database import get_products,get_sales,get_stocks,insert_products,insert_sales,insert_stock, check_available_stock

# Flask Instance : because "app" is an object and an object is an instance of a class.
# "Flask" is a class
app = Flask(__name__)

@app.route('/')
def home():
    number=100
    return render_template("index.html", x = number)

@app.route('/products')
def products():
    products_data=get_products()
    return render_template("products.html", products_data = products_data)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product=(product_name,buying_price,selling_price)
        insert_products(new_product)
        print("Product added successfully")

    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales_data=get_sales()
    products=get_products()
    return render_template("sales.html",sales_data = sales_data,products = products)

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['qt']

        new_sale=(product_id,quantity)
        available_stock=check_available_stock(product_id)

        if available_stock < float(quantity):
            print("Insufficent stock,add more.")
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        print("Sale added successfully")
        return redirect(url_for('sales'))
    
    return redirect(url_for('sales'))
    

@app.route('/stock')
def stock():
    stocks_data=get_stocks()
    products=get_products()
    return render_template("stock.html", stocks_data = stocks_data,products = products)

@app.route('/add_stocks',methods=['GET','POST'])
def add_stocks():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['stock_qt']

        new_stock=(product_id,quantity)
        insert_stock(new_stock)
        print("Stock added successfully")

    return redirect(url_for('stock'))

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

# Run your application
app.run()