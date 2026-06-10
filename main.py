from flask import Flask, render_template

# Flask Instance : because "app" is an object and an object is an instance of a class.
# "Flask" is a class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/sales')
def sales():
    return render_template("sales.html")

@app.route('/stock')
def stock():
    return render_template("stock.html")

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