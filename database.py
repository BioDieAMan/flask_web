
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'newtest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def db_init():
    db.create_all()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tempreture = db.Column(db.Float(), unique=True)
    longitude = db.Column(db.Float(), unique=True)
    latitude = db.Column(db.Float(), unique=True)

    def __init__(self, tempreture, email, longitude, latitude):
        self.tempreture = tempreture
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return '<User %r>' % self.usernam


# @app.route('/')
# def home():
#     return render_template('index.html')


# if __name__ == '__main__':
#     db.cr
#     app.run(debug=True)
