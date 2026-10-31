from flask import Flask, render_template, request, redirect, session
import sqlite3

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
    
    r = con.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, pass_word))
    c = r.fetchone()
    
    if c:
        session['username'] = user # 👈 ذخیره در حافظه
        return redirect('/dashboard')
    else:
        return "نام کاربری یا رمز عبور اشتباه است!"

@app.route('/logout')
def logout():
    session.pop('username', None) # 👈 پاک کردن از حافظه
    return redirect('/')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    con.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pass_word))
    con.commit()
    
    return f"کاربر {user} با موفقیت ثبت نام شد! <br><a href='/'>برو به صفحه ورود</a>"

if __name__ == '__main__':
    app.run(debug=True)