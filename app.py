from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super_secret_key'
con = sqlite3.connect("user.db", check_same_thread=False)

# ساخت جدول
con.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
con.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/')
    cursor = con.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('dashboard.html', users=users)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    r = con.execute("SELECT * FROM users WHERE username = ?", (user,))
    c = r.fetchone()
    
    # چک کردن رمز هش شده
    if c and check_password_hash(c[1], pass_word):
        session['username'] = user
        return redirect('/dashboard')
    else:
        return "نام کاربری یا رمز عبور اشتباه است!"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    # هش کردن رمز
    hashed_pass = generate_password_hash(pass_word)
    
    con.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, hashed_pass))
    con.commit()
    
    return f"کاربر {user} با موفقیت ثبت نام شد! <br><a href='/'>برو به صفحه ورود</a>"

@app.route('/delete/<username>')
def delete_user(username):
    if 'username' not in session:
        return redirect('/')
    con.execute("DELETE FROM users WHERE username = ?", (username,))
    con.commit()
    return redirect('/dashboard')

@app.route('/products')
def products_page():
    if 'username' not in session:
        return redirect('/')
    # خواندن همه محصولات از دیتابیس
    cursor = con.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    if 'username' not in session:
        return redirect('/')
    # گرفتن نام و قیمت از فرم
    name = request.form.get('name')
    price = request.form.get('price')
    
    con.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    con.commit()
    
    return redirect('/products')

@app.route('/delete_product/<int:id>')
def delete_product(id):
    if 'username' not in session:
        return redirect('/')
    # حذف محصول بر اساس ID
    con.execute("DELETE FROM products WHERE id = ?", (id,))
    con.commit()
    
    return redirect('/products')

if __name__ == '__main__':
    app.run(debug=True)