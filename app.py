from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("user.db", check_same_thread=False)

# ساخت جدول
con.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

# ساخت کاربر تستی (فقط برای بار اول)
#con.execute("INSERT INTO users (username, password) VALUES ('admin', '123456')")
#con.commit()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    r = con.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, pass_word))
    c = r.fetchone()
    
    if c:
        return redirect('/dashboard')  # 👈 هدایت به داشبورد
    else:
        return "نام اشتباه است"

if __name__ == '__main__':
    app.run(debug=True)