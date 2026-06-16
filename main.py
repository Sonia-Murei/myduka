from flask import Flask, render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stocks,insert_products,insert_sales,insert_stock, check_available_stock,check_user_exists,create_user
from flask_bcrypt import Bcrypt

# Flask Instance : because "app" is an object and an object is an instance of a class.
# "Flask" is a class
app = Flask(__name__)

# Bcrypt instance with flask app (object)
bcryp = Bcrypt(app)

app.secret_key = '8fw84rh48ehd89qhf8rh4pqh8r9q'

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
        flash("Product added successfully",'success') #'success' is the category

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
            flash("Insufficent stock,add more.",'danger')
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        flash("Sale added successfully",'success')
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
        flash("Stock added successfully",'success')

    return redirect(url_for('stock'))

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.form == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcryp.generate_password_hash(password).decode('utf-8') 
            #.decode converts bytes to strings
            # takes every character from every (human) language into one representation using numbers.
            new_user = (full_name,email,phone_number,hashed_password)
            create_user(new_user)
            flash("User created successfully",'success')
            return redirect(url_for('login'))
        else:
            flash("User already exists,please login instead",'danger')

    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

# Run your application
app.run()