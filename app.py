from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("user.db", check_same_thread=False)

# ساخت جدول
con.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

# صفحه ورود
@app.route('/')
def home():
    return render_template('index.html')

# صفحه داشبورد
@app.route('/dashboard')
def dashboard():
    cursor = con.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('dashboard.html', users=users)

# پردازش فرم ورود
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    r = con.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, pass_word))
    c = r.fetchone()
    
    if c:
        return redirect('/dashboard')
    else:
        return "نام کاربری یا رمز عبور اشتباه است!"

# نمایش صفحه ثبت نام
@app.route('/register')
def register_page():
    return render_template('register.html')

# پردازش فرم ثبت نام
@app.route('/register', methods=['POST'])
def register():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    # ذخیره در دیتابیس
    con.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pass_word))
    con.commit()
    
    return f"کاربر {user} با موفقیت ثبت نام شد! <br><a href='/'>برو به صفحه ورود</a>"

if __name__ == '__main__':
    app.run(debug=True)