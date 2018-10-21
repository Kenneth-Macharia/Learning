class Student(object):

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average_mark(self):
        return sum(self.marks)/len(self.marks)

    def going_to_school(self):
        print('I am going to {}.'.format(self.school))

# anna = Student('Anna', 'MIT')
# anna.marks.append(56)
# anna.marks.append(74)
# anna.marks.append(78)
# print(anna.name, anna.average_mark())
# anna.going_to_school()


class Store(object):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        new_item = {'name':name, 'price':price}
        self.items.append(new_item)

    def get_items(self):
        return [items for items in self.items]

    def stock_price(self):
        return sum([items['price'] for items in self.items])

    @classmethod
    def franchise(cls, store):
        return Store(store.name + ' - franchise')

    @staticmethod
    def store_details(store):
        return '{} store total stock is {}'.format(store.name, int(store.stock_price()))

# store1 = Store('Tuskys')
# store1.add_item('sugar',100)
# store1.add_item('salt',30)
# store1.add_item('bread',50)
# print(store1.name, store1.get_items(), store1.stock_price())

store1 = Store('Tuskys')
store1.add_item('sugar',100)
store1.add_item('salt',30)
store1.add_item('bread',50)
print(Store.franchise('Nakumatt'))
print(Store.store_details('Naivas'))
