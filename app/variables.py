from app.Classes import Shop, Customer
from app.file_reader import json_reader


info = json_reader()
fuel_price = info["FUEL_PRICE"]

Alex = Customer('Alex', {'milk': 2, 'bread': 2, 'butter': 2},
                {'milk': 0, 'bread': 0, 'butter': 0},
                [1, -2], 41, {'brand': 'BMW', 'fuel_consumption': 9.1})

Bob = Customer('Bob', {'milk': 4, 'bread': 2, 'butter': 5},
               {'milk': 0, 'bread': 0, 'butter': 0},
               [12, -2], 55, {'brand': 'Suzuki', 'fuel_consumption': 9.9})

Monica = Customer('Monica', {'milk': 3, 'bread': 3, 'butter': 1},
                  {'milk': 0, 'bread': 0, 'butter': 0},
                  [11, -2], 12, {'brand': 'Audi', 'fuel_consumption': 7.6})

Shop_24_7 = Shop("Shop '24/7'", [4, 3],
                 {'milk': 2, 'bread': 1.5, 'butter': 3.2})

Central_Shop = Shop('Central Shop', [0, 0],
                    {'milk': 3, 'bread': 2, 'butter': 3.5})

Outskirts_Shop = Shop('Outskirts Shop', [10, -5],
                      {'milk': 3, 'bread': 1, 'butter': 2.5})

customers = [Bob, Alex, Monica]
shops = [Shop_24_7, Outskirts_Shop, Central_Shop]
