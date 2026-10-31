from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super_secret_key' # 👈 این خط خیلی مهمه
con = sqlite3.connect("user.db", check_same_thread=False)

# ساخت جدول
con.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # چک کردن اینکه کاربر لاگین کرده یا نه
    if 'username' not in session:
        return redirect('/')
        
    cursor = con.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('dashboard.html', users=users)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    # 👈 اول فقط بر اساس اسم کاربر رو پیدا کن
    r = con.execute("SELECT * FROM users WHERE username = ?", (user,))
    c = r.fetchone()
    
    # 👈 اگه کاربر پیدا شد و رمزش با هش دیتابیس مطابقت داشت:
    if c and check_password_hash(c[1], pass_word):
        session['username'] = user
        return redirect('/dashboard')
    else:
        return "نام کاربری یا رمز عبور اشتباه است!"

@app.route('/logout')
def logout():
    session.pop('username', None) # 👈 پاک کردن از حافظه
    return redirect('/')

@app.route('/delete/<username>')
def delete_user(username):
    # چک کردن اینکه فقط کاربر لاگین کرده بتونه حذف کنه
    if 'username' not in session:
        return redirect('/')
        
    con.execute("DELETE FROM users WHERE username = ?", (username,))
    con.commit()
    
    return redirect('/dashboard')

@app.route('/register', methods=['POST'])
def register():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    # 👈 تبدیل رمز به هش (غیرقابل خوندن)
    hashed_pass = generate_password_hash(pass_word)
    
    con.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, hashed_pass))
    con.commit()
    
    return f"کاربر {user} با موفقیت ثبت نام شد! <br><a href='/'>برو به صفحه ورود</a>"

