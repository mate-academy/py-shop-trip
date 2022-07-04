import json
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Shop:
    name: str
    location: list
    products: dict

    @classmethod
    def create_shop(cls, file_name):
        with open(file_name, "r") as f_json:
            info = json.load(f_json)
            lst_shop = []
            for shop in info["shops"]:
                lst_shop.append(cls(name=shop["name"],
                                    location=shop["location"],
                                    products=shop["products"]))
            return lst_shop

    def print_bill(self, other):
        now = datetime.now()
        total_milk = other.product_cart['milk'] * self.products['milk']
        total_bread = other.product_cart['bread'] * self.products['bread']
        total_butter = other.product_cart['butter'] * self.products['butter']
        total_product = total_milk + total_bread + total_butter
        return f"""Date: {now.strftime('%Y/%m/%d %H:%M:%S')}  
Thanks, {other.name}, for you purchase!  
You have bought: 
{other.product_cart['milk']} milks for {total_milk} dollars  
{other.product_cart['bread']} breads for {total_bread} dollars  
{other.product_cart['butter']} butters for {total_butter} dollars  
Total cost is {total_product} dollars  
See you again!"""
