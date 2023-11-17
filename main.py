from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template('home.html', year=year, title="cows")

@app.route('/address')
def address():
    return render_template('address.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
