from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'super_secret_key'
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
    if 'username' not in session:  # 👈 اگه توی حافظه نبود
        return redirect('/')       # 👈 بفرستش به صفحه لاگین
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
        session['username'] = user  
        return redirect('/dashboard')
    else:
        return "نام کاربری یا رمز عبور اشتباه است!"

# نمایش صفحه ثبت نام
@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None) # پاک کردن اسم از حافظه
    return redirect('/')

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