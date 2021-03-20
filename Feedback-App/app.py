from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

# Things to find out
    # Did I set up the url database incorrectly? Read documentations 
    # Create feedback table. In terminal try (from app import)?

if ENV == 'dev':
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URL"] = 'postgresql://postgres:Iwantbetter21@localhost/comments'
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URL"] = ''

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] - False

    db = SQLAlchemy(app)

    class Feedback(db.Model):
        __tablename__ = 'feedback'
        id = db.Colum(db.Integer, primary_key=True)
        customer = db.Column(db.String(200), unique=True)
        rating = db.Colum(db,Integer)
        business = db.Colum(db.String(200))
        comments = db.Colum(db.Text())

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
