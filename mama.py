class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {"name": name, "pri  ce": price}
        self.items.append(item)
    def stock_price(self):
        list = [item['price'] for item in self.items]
        print(list)
        return sum(list)
store = Store('ceva')
store.add_item('test',25.0)
store.add_item('test3',255.0)
print(store.stock_price())