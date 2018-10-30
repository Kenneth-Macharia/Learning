''' This module contains helper model for interacting with items '''

from sqlalchemy_init import db_obj


class ItemModel(db_obj.Model):
    #Tell sqlalchemy where the models will be stored i.e. table & columns
    __tablename__ = 'items_table'

    id = db_obj.Column(db_obj.Integer, primary_key=True)
    name = db_obj.Column(db_obj.String(80))  #Character length
    price = db_obj.Column(db_obj.Float(precision=2))  #Decimal number to two decimal places

    ''' This col specifies the store to which the item model belongs to,
        linked by the foreign_key with the primary_key in the store model. '''

    store_id = db_obj.Column(db_obj.Integer, db_obj.ForeignKey('store_table.id'))
    store = db_obj.relationship('StoreModel') #Finds the related store by the store_id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def get_json_item(self):
        return {'id':self.id, 'name':self.name, 'price':self.price, 'store':self.store_id}  #returns a json rep of the model i.e items

    @classmethod
    def find_item_by_name(cls, name):
        # Below equivalent: SELECT * FROM items_table WHERE name=name LIMIT 1 ie. first row only '''
        # Below also convert the retruend row into an ItemModel object with its attributes 'id, name & price'
        return cls.query.filter_by(name=name).first()

    def save_item(self):   #change name as it can perfom add & update
        # We just instruct sqlalchemy to insert an object
        # A session is a colelction of objects to add, which can all be written at once
        # This will be used to update an objects's attribute as well
        db_obj.session.add(self)
        db_obj.session.commit()

    def delete_item(self):  #change to delete method
        db_obj.session.delete(self)
        db_obj.session.commit()
