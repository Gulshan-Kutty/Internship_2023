import os
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

########### SQL Alchemy Configuration ###########

basedir = os.path.abspath(os.path.dirname(__file__))  # os.path.dirname(__file__) ---> this will fetch the directory name where app.py is present and that directory is app_10
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # passing application to SQL Alchemy
Migrate(app,db)


############### Create a Model ##################

class Sabji(db.Model):
    __tablename__ = 'sabjis'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    mrp = db.Column(db.Integer)

    def __init__(self, name, mrp):
        self.name = name
        self.mrp = mrp
    def __repr__(self):
        return "Sabji Name - {} and MRP - {}".format(self.name, self.mrp)


#################################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['GET','POST'])
def add():
    if request.method == 'POST':
       name = request.form.get('in_1') 
       mrp = request.form.get('in_2')

       new_sabji = Sabji(name, mrp)
       db.session.add(new_sabji)
       db.session.commit()

    return render_template('add.html')

@app.route('/search')
def search():
    name = request.args.get('in_1')
    sabji = Sabji.query.filter_by(name=name).first()
    return render_template('search.html', sabji=sabji)

@app.route('/display')
def display_all():
    sabjis = Sabji.query.all()   # it's like select * from table
    return render_template('display.html', sabjis = sabjis)

if __name__ == '__main__':
    app.run(debug=True)


