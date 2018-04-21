from peewee import *

database = SqliteDatabase('data-2017-2018.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Home(BaseModel):
    _of_baths = FloatField(column_name='# OF BATHS', null=True)
    _of_beds = IntegerField(column_name='# OF BEDS', null=True)
    _of_fireplaces = IntegerField(column_name='# OF FIREPLACES', null=True)
    basement_type = IntegerField(column_name='BASEMENT TYPE', null=True)
    building_style = IntegerField(column_name='BUILDING STYLE', null=True)
    census_tract = IntegerField(column_name='CENSUS TRACT', null=True)
    council_district = TextField(column_name='COUNCIL DISTRICT', null=True)
    deed_book = TextField(column_name='DEED BOOK', null=True)
    deed_date = TextField(column_name='DEED DATE', null=True)
    deed_page = IntegerField(column_name='DEED PAGE', null=True)
    depth = FloatField(column_name='DEPTH', null=True)
    front = FloatField(column_name='FRONT', null=True)
    heat_type = IntegerField(column_name='HEAT TYPE', null=True)
    house_number = IntegerField(column_name='HOUSE NUMBER', null=True)
    land_value = IntegerField(column_name='LAND VALUE', null=True)
    location = TextField(column_name='LOCATION', null=True)
    mail1 = FloatField(column_name='MAIL1', null=True)
    mail2 = FloatField(column_name='MAIL2', null=True)
    mail3 = TextField(column_name='MAIL3', null=True)
    mail4 = TextField(column_name='MAIL4', null=True)
    overall_condition = IntegerField(column_name='OVERALL CONDITION', null=True)
    owner1 = TextField(column_name='OWNER1', null=True)
    owner2 = FloatField(column_name='OWNER2', null=True)
    previous_property_class = IntegerField(column_name='PREVIOUS PROPERTY CLASS', null=True)
    prop_class_description = TextField(column_name='PROP CLASS DESCRIPTION', null=True)
    property_class = IntegerField(column_name='PROPERTY CLASS', null=True)
    roll_section = IntegerField(column_name='ROLL SECTION', null=True)
    sale_price = IntegerField(column_name='SALE PRICE', null=True)
    sbl = FloatField(column_name='SBL', null=True)
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

