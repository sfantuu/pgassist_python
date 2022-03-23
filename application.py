#Imports
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

#Create a Flask instance
app = Flask(__name__)
#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goblincakessale.sqlite'
#Ignore Warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initialize the database
db = SQLAlchemy(app)

#new session
Session = sessionmaker(bind=db.engine)
session = Session()

#Create Model
class GoblinCakes(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String, nullable=False)
    product_type = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    units_sold = db.Column(db.Integer, nullable=False)
    quarter = db.Column(db.Integer, nullable=False)

    #create string template to add data to the SQL
    def __repr__(self, id, product, product_type, price, units_sold, quarter):
        self.id = id
        self.product = product
        self.product_type = product_type
        self.price = price
        self.units_sold = units_sold
        self.quarter = quarter


#add data to the database
#simple function to add all the tables in sqlite
def add_data():
    session.add_all([
    GoblinCakes(id = 1,product= 'Hobgoblin', product_type = 'Cake', price = 4, units_sold = 388, quarter = 1),
    GoblinCakes(id = 2,product= 'Green Goblin', product_type = 'Cake', price = 4,units_sold = 312, quarter = 1),
    GoblinCakes(id = 3,product= 'Forest Sprite', product_type = 'Canned Drink', price = 0.8, units_sold = 97,quarter = 1),
    GoblinCakes(id = 4,product= 'Redcap', product_type = 'Cake', price = 3.5, units_sold = 605,quarter = 1),
    GoblinCakes(id = 5,product= 'Imp', product_type = 'Cake', price = 2, units_sold = 162, quarter = 1),

    GoblinCakes(id = 6,product= 'Hobgoblin', product_type = 'Cake', price = 4, units_sold=482,quarter = 2),
    GoblinCakes(id = 7,product= 'Green Goblin', product_type = 'Cake', price = 4, units_sold=312,quarter = 2),
    GoblinCakes(id = 8,product= 'Forest Sprite', product_type = 'Canned Drink', price = 0.8,units_sold=123,quarter = 2),
    GoblinCakes(id = 9,product= 'Redcap', product_type =  'Cake', price = 4, units_sold=401,quarter = 2),
    GoblinCakes(id = 10,product= 'Imp', product_type = 'Cake', price = 1.5, units_sold=540,quarter = 2),
    GoblinCakes(id = 11,product= 'Filthy Hobbit', product_type = 'Cookie',price = 1,units_sold=325,quarter = 2),

    GoblinCakes(id = 12,product='Hobgoblin', product_type = 'Cake',price = 4,units_sold=389,quarter = 3),
    GoblinCakes(id = 13,product='Green Goblin', product_type = 'Cake',price = 4,units_sold=302,quarter = 3),
    GoblinCakes(id = 14,product='Forest Sprite', product_type = 'Canned Drink',price = 0.8,units_sold=168,quarter = 3),
    GoblinCakes(id = 15,product='Redcap', product_type = 'Cake',price = 4,units_sold=433,quarter = 3),
    GoblinCakes(id = 16,product='Imp', product_type = 'Cake',price = 2,units_sold=486,quarter = 3),
    GoblinCakes(id = 17,product='Filthy Hobbit', product_type = 'Cookie',price = 1,units_sold=164,quarter = 3),
    GoblinCakes(id = 18,product='Wretched Elf', product_type = 'Cookie',price = 1,units_sold=212,quarter = 3),
    GoblinCakes(id = 19,product='Foul Dwarf', product_type = 'Cookie',price = 1,units_sold=168,quarter = 3),
    GoblinCakes(id = 20,product='Vile Human', product_type = 'Cookie',price = 1,units_sold=92,quarter = 3),

    GoblinCakes(id = 21,product='Hobgoblin', product_type = 'Cake',price = 4,units_sold=369,quarter = 4),
    GoblinCakes(id = 22,product='Green Goblin', product_type = 'Cake',price = 4,units_sold=333,quarter = 4),
    GoblinCakes(id = 23,product='Forest Sprite', product_type = 'Canned Drink',price = 0.8,units_sold=168,quarter = 4),
    GoblinCakes(id = 24,product='Redcap', product_type = 'Cake',price = 4,units_sold=462,quarter = 4),
    GoblinCakes(id = 25,product='Imp', product_type = 'Cake',price = 2,units_sold=501,quarter = 4),
    GoblinCakes(id = 26,product='Filthy Hobbit', product_type = 'Cookie',price = 1,units_sold=125,quarter = 4),
    GoblinCakes(id = 27,product='Wretched Elf', product_type = 'Cookie',price = 1,units_sold=201,quarter = 4),
    GoblinCakes(id = 28,product='Foul Dwarf', product_type = 'Cookie',price = 1,units_sold=162,quarter = 4),
    GoblinCakes(id = 29,product='Vile Human', product_type = 'Cookie',price = 1,units_sold=143,quarter = 4),
    GoblinCakes(id = 30,product='Wizard Spit', product_type = 'Hot Drink',price = 3.5,units_sold=455,quarter = 4),
    GoblinCakes(id = 31,product='Brownie', product_type = 'Cake',price = 1.5,units_sold=666,quarter = 4)
])
    #save the changes to the database
    session.commit()


#Use only the GET method since we just need to receive data, not modify
#Setting a route defined as "/"
#Query using a filter to display only cakes
@app.route("/", methods=["GET"])
def goblins():
    if request.method == "GET":
        return render_template("index.html", query=GoblinCakes.query.filter(GoblinCakes.product_type == 'Cake').all())

#Use only the GET method since we just need to receive data, not modify
#Setting a route defined as "/firstquarter"
#Query using a filter to display only cakes by 1st quarter
@app.route("/firstquarter", methods=["GET"])
def firstquarter():
    if request.method == "GET":
        return render_template("firstquarter.html", query=GoblinCakes.query.filter(GoblinCakes.product_type == 'Cake' , GoblinCakes.quarter =='1').all())

#Use only the GET method since we just need to receive data, not modify
#Setting a route defined as "/secondquarter"
#Query using a filter to display only cakes by quarter 2
@app.route("/secondquarter", methods=["GET"])
def secondquarter():
    if request.method == "GET":
        return render_template("secondquarter.html", query=GoblinCakes.query.filter(GoblinCakes.product_type == 'Cake', GoblinCakes.quarter =='2').all())

#Use only the GET method since we just need to receive data, not modify
#Setting a route defined as "/thirdquarter"
#Query using a filter to display only cakes by quarter 3
@app.route("/thirdquarter", methods=["GET"])
def thirdquarter():
    if request.method == "GET":
        return render_template("thirdquarter.html", query=GoblinCakes.query.filter(GoblinCakes.product_type == 'Cake', GoblinCakes.quarter =='3').all())

#Use only the GET method since we just need to receive data, not modify
#Setting a route defined as "/fourthquarter"
#Query using a filter to display only cakes by quarter 4
@app.route("/fourthquarter", methods=["GET"])
def fourthquarter():
    if request.method == "GET":
        return render_template("fourthquarter.html", query=GoblinCakes.query.filter(GoblinCakes.product_type == 'Cake', GoblinCakes.quarter =='4').all())



#App run
#Setting the port for 8000
if __name__ == "__main__":
    app.run(debug=True, port=8000)