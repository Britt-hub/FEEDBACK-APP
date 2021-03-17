from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        rating = request.form['rating']
        business = request.form['business']
        comments = request.form['comments']
        print(customer, rating, business, comments)
        if customer == '' or business == '':
            return render_template('index.html', message="Please enter required fields.")
        return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
