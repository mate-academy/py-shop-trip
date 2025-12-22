import json
from app.shop import Shop
from app.Customer import Customer


def shop_trip():
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    
    shops = []
    for shop_data in config["shops"]:
        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )
        shops.append(shop)
    
    customers = []
    for customer_data in config["customers"]:
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            customer_data["car"],
            customer_data["location"]
        )
        customers.append(customer)
    
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        
        cheapest_shop, cheapest_cost = customer.find_cheapest_shop(shops, fuel_price)
        
        if customer.money >= cheapest_cost:
            customer.travel_to(cheapest_shop)
            customer.purchase(cheapest_shop, cheapest_cost)
            customer.go_home()
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")