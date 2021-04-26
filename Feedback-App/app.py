from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'


# Things to find out
# Did I set up the url database incorrectly? Read documentations
# Create feedback table. In terminal try (from app import)?
# Using mySQL 


db_path = "mysql://root:root@localhost:3306/feedback_app_db"
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path 
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URL'] = ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# this is code is not working

  class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    rating = db.Column(db, Integer)
    business = db.Column(db.String(200))
    comments = db.Column(db.Text())

   def __init__(self, customer, rating, business, comments):
    self.customer = customer
    self.rating = rating
    self.business = business
    self.comments = comments


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
    app.run()
