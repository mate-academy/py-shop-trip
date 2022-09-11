from app.customer import Customer
from app.shop import Shop


def shop_trip():
    fuel_price = Customer.information["FUEL_PRICE"]
    for customer in Customer.information["customers"]:
        food_and_trip_price = 9999999999999
        shop_name = None
        trip_price = 0
        bought_products = []
        name = customer["name"]
        money = customer["money"]
        fuel_consumption = customer["car"]["fuel_consumption"]
        person_location = customer["location"]
        Customer.person_money(name, money)
        customer_products = customer["product_cart"]
        milk_amount = customer_products["milk"]
        bread_amount = customer_products["bread"]
        butter_amount = customer_products["butter"]
        for shop in Customer.information["shops"]:
            total_price = 0
            current_shop_name = shop["name"]
            shop_location = shop["location"]
            distance_to_the_shop = Customer.two_points(person_location,
                                                       shop_location) * 2
            fuel_cost = Customer.fuel_cost(fuel_price, fuel_consumption)
            current_trip_price = round(distance_to_the_shop * fuel_cost, 2)
            total_price += current_trip_price
            milk_price = shop["products"]["milk"]
            bread_price = shop["products"]["bread"]
            butter_price = shop["products"]["butter"]
            all_milk_price = milk_price * milk_amount
            all_bread_price = bread_price * bread_amount
            all_butter_price = butter_price * butter_amount
            total_price += all_milk_price + all_bread_price + all_butter_price
            Shop.total_shop_price(name, current_shop_name, total_price)
            if total_price < food_and_trip_price:
                bought_products.clear()
                food_and_trip_price = total_price
                shop_name = current_shop_name
                trip_price = current_trip_price
                bought_products.append(["milks", milk_amount,
                                        all_milk_price])
                bought_products.append(["breads", bread_amount,
                                        all_bread_price])
                bought_products.append(["butters", butter_amount,
                                        all_butter_price])

        Customer.checking_money(name, shop_name, money,
                                food_and_trip_price)
        if money >= food_and_trip_price:
            Shop.bought_products(bought_products,
                                 name,
                                 round
                                 (food_and_trip_price - trip_price, 2))
            money_left = customer["money"]
            money_left -= food_and_trip_price
            Customer.trip_home(name, money_left)
