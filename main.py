from flask import Flask, render_template
from database import get_products,get_sales,get_stocks

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

@app.route('/sales')
def sales():
    sales_data=get_sales()
    return render_template("sales.html",sales_data = sales_data)

@app.route('/stock')
def stock():
    stocks_data=get_stocks()
    return render_template("stock.html", stocks_data = stocks_data)

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