import os
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import json
from werkzeug.utils import secure_filename
from peewee import *
#from mymodels import Home
#from flask_cors import CORS

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.debug = True
#app.secret_key = 'sUpa SecRet thso Key'
app.secret_key = os.urandom(24)

db = SqliteDatabase('data-2017-2018.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = db

class Home(BaseModel):
    _of_baths = TextField(column_name='# OF BATHS', null=True)
    _of_beds = IntegerField(column_name='# OF BEDS', null=True)
    _of_fireplaces = IntegerField(column_name='# OF FIREPLACES', null=True)
    basement_type = IntegerField(column_name='BASEMENT TYPE', null=True)
    building_style = IntegerField(column_name='BUILDING STYLE', null=True)
    census_tract = IntegerField(column_name='CENSUS TRACT', null=True)
    council_district = TextField(column_name='COUNCIL DISTRICT', null=True)
    deed_book = TextField(column_name='DEED BOOK', null=True)
    deed_date = TextField(column_name='DEED DATE', null=True)
    deed_page = IntegerField(column_name='DEED PAGE', null=True)
    depth = TextField(column_name='DEPTH', null=True)
    front = TextField(column_name='FRONT', null=True)
    heat_type = IntegerField(column_name='HEAT TYPE', null=True)
    house_number = IntegerField(column_name='HOUSE NUMBER', null=True)
    land_value = IntegerField(column_name='LAND VALUE', null=True)
    location = TextField(column_name='LOCATION', null=True)
    mail1 = TextField(column_name='MAIL1', null=True)
    mail2 = TextField(column_name='MAIL2', null=True)
    mail3 = TextField(column_name='MAIL3', null=True)
    mail4 = TextField(column_name='MAIL4', null=True)
    overall_condition = IntegerField(column_name='OVERALL CONDITION', null=True)
    owner1 = TextField(column_name='OWNER1', null=True)
    owner2 = TextField(column_name='OWNER2', null=True)
    previous_property_class = IntegerField(column_name='PREVIOUS PROPERTY CLASS', null=True)
    prop_class_description = TextField(column_name='PROP CLASS DESCRIPTION', null=True)
    property_class = IntegerField(column_name='PROPERTY CLASS', null=True)
    roll_section = IntegerField(column_name='ROLL SECTION', null=True)
    sale_price = IntegerField(column_name='SALE PRICE', null=True)
    sbl = TextField(column_name='SBL', null=True)
    sbl_number = TextField(column_name='SBL NUMBER', null=True)
    street = TextField(column_name='STREET', null=True)
    tax_district = IntegerField(column_name='TAX DISTRICT', null=True)
    total_living_area = IntegerField(column_name='TOTAL LIVING AREA', null=True)
    total_value = IntegerField(column_name='TOTAL VALUE', null=True)
    year_built = IntegerField(column_name='YEAR BUILT', null=True)
    zip_code_4_digit_ = IntegerField(column_name='ZIP CODE (4-DIGIT)', null=True)
    zip_code_5_digit_ = IntegerField(column_name='ZIP CODE (5-DIGIT)', null=True)

    class Meta:
        table_name = 'Home'
        primary_key = False


db.connect()

# class Home(Model):
#     sbl = CharField()
#     tax_district = CharField()
#     sbl_number = CharField()
#     front = CharField(null = True)

#     class Meta:
#         database = db # This model uses the "people.db" database.

#db.create_tables([Pothole])

@app.route("/")
def hello():
    #query = Home.select()
    # query = Home.select().where(Home.location.contains('112 Peter'))
    # for q in query:
    #   print(q.location)
    return render_template('index.html')

@app.route("/getData", methods=['POST'])
def getData():
    if request.method == 'POST':
       print(request.values['address'])
       addy = request.values['address']
       query = Home.select().where(Home.location.contains(addy)).dicts().get()
       #for q in query:
       # print(q.location)
    return jsonify(query)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
       print(request.values['address'])
       #spec = jsonify(request.data)
       spec = json.loads(str(request.data.decode('utf-8')))
       pic = spec['pic']
       center = spec['lat']
       location = spec['lon']
       p = Pothole(pic = pic, lat = center, lon = location, city = location)
       p.save()
       return jsonify({'success': 'success'})

@app.route('/potholes', methods=['GET'])
def get():
	potholes = Pothole.select()
	p2 = []
	for p in potholes:
		p2.append([p.pic])
	db.close()
	kobe='kobe'
	print(p2)
	return jsonify({'potholes':p2})



if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)

app.debug = True
#CORS(app)
app.run(threaded=True,host='0.0.0.0',port=5000)
#CORS(app)