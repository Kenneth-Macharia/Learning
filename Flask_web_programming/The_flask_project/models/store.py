''' This module contains the store model '''
''' Sqlite limitations as opposed to the main stream engines e.g Postgresql, MySql:
    1. It can't do simulteanous write operations to the dbase
    2. Does nto enforce foreign key relationships, i.e a table value dependent on another,
        can be written to without the independent table value being present in the table '''
from sqlalchemy_init import db_obj


class StoreModel(db_obj.Model):
    __tablename__ = 'store_table'

    id = db_obj.Column(db_obj.Integer, primary_key=True)
    name = db_obj.Column(db_obj.String(80))

    ''' When a store model is created, then an obj is created for each item
        that is related to the store, which can be a computationally intensive
        operation if there are many store and related items <Options 1>'''
    ''' Instead create a query builder that instead only searches the db
        for the required items realted to a particular store and SLQAlchemy
        creates obj for only those. <Options 2'''
    ''' The trade of between the two options is between creating the obj list first
        then iterating over it on each request <option 1> but accessing the db just once
        or accessing the db only when we need to retrieve items but having
        to access it for each request <option 2> '''
    ''' Thus the trade-off is between, number of items vs number of requests '''

    store_items = db_obj.relationship('ItemModel')  # <Option 1 : This creates an objs list
    #store_items = db_obj.relationship('ItemModel', lazy='dynamic') # <Option 2> : This creates a query builder

    def __init__(self, name):
        self.name = name

    def get_json_store(self):
        return {'id':self.id, 'name':self.name, 'items':[items.get_json_store() for items in self.store_items]}  # <Option 1>
        #return {'name':self.name, 'items':[items.get_json_store() for items \
        #in store_items.all()]}  #<Option 2>

    @classmethod
    def find_store_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_store(self):
        db_obj.session.add(self)
        db_obj.session.commit()

    def delete_store(self):
        db_obj.session.delete(self)
        db_obj.session.commit()
