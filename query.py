"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
db.session.query(Model).filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
db.session.query(Brand).filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903 and Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
from sqlalchemy import or_
Brand.query.filter(or_(Brand.discontinued==None, Brand.founded<1950)).all()

# Get all models whose brand_name is not Chevrolet.
db.session.query(Model).filter(Model.brand_name!='Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    outputs = Model.query.filter(Model.year == year).all()

    for output in outputs:
        print output.name, output.brand_name, output.brand.headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    outputs = db.session.query(Model.name, Model.brand_name).distinct().order_by(Model.brand_name).all()

    for output in outputs:
        print output.brand_name, output.name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
    Returned value: <flask_sqlalchemy.BaseQuery object at 0x7fdbfc435350>
    The datatype is an object

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
    When 2 classes share a many-to-many relationship new table is created to represent their common associations, including a foreign key from each table.
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands_like = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()
    print brands_like

def get_models_between(start_year, end_year):
    models_during = Model.query.filter(Model.year>start_year, Model.year<end_year).all()
