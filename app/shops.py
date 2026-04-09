class Shop:
    def __init__(self,name, location, products: dict):
        self.name = name
        self.location = location
        self.products = products

def create_stores(list_shops):
    shops = {}
    for shop in list_shops:
        shops[shop["name"]] = Shop(shop["name"], shop["location"], shop["products"])
    return shops

