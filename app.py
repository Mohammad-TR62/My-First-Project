from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("user.db", check_same_thread=False)
con.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
@app.route('/')
def home():
    return render_template('index.html')

# مسیر جدید برای دریافت اطلاعات فرم
@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pass_word = request.form.get('password')
    
    print("--- CHECK ---")
    print("User:", user)
    print("Pass:", pass_word)
    
    r = con.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, pass_word))
    c = r.fetchone()
    
    print("DB Result:", c)
    print("-------------")

    if c:
        return f"سلام {user}! ورود با موفقیت انجام شد."
    #else:
    #    return "نام اشتباه است"

if __name__ == '__main__':
    app.run(debug=True)