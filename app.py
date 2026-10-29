from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Salam! In avalin site man ast.</h1><p>Man daram Flask yad migiram.</p>"

if __name__ == '__main__':
    app.run(debug=True)