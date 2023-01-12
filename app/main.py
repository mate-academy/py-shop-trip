from app.shop import create_class_instance_shops_list
from app.customers import create_class_instance_customers_list
from app.info import get_information


def shop_trip() -> None:
    shops_list = create_class_instance_shops_list()
    customers_list = create_class_instance_customers_list()
    fuel_price = get_information()["FUEL_PRICE"]

    for customer in customers_list:
        shops_cost = []
        shops = []

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops_list:
            shop_dict = {}
            distance_x = shop.location[0] - customer.location[0]
            distance_y = shop.location[1] - customer.location[1]
            distance_to_shop = (distance_x ** 2 + distance_y ** 2) ** (1 / 2)
            shop_dict["travel_cost"] = distance_to_shop \
                * customer.car_fuel_consumption_per_km * fuel_price

            shop_dict["milk_money"] = customer.product_cart["milk"] \
                * shop.products["milk"]
            shop_dict["bread_money"] = customer.product_cart["bread"] \
                * shop.products["bread"]
            shop_dict["butter_money"] = customer.product_cart["butter"] \
                * shop.products["butter"]
            shop_dict["products_money"] = shop_dict["milk_money"] \
                + shop_dict["bread_money"] \
                + shop_dict["butter_money"]

            final_cost = shop_dict["products_money"] \
                + (shop_dict["travel_cost"] * 2)
            final_cost = round(final_cost * 100) / 100
            shop_dict["final_cost"] = final_cost

            shop_dict["name"] = shop.name
            shop_dict["location"] = shop.location

            shops.append(shop_dict)
            shops_cost.append(final_cost)

            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {final_cost}")

        cheapest_shop_cost = 0
        cheapest_shop = {}
        for i in range(len(shops_cost)):
            if shops_cost[i] == min(shops_cost):
                cheapest_shop_cost = shops_cost[i]
                cheapest_shop = shops[i]
                break
        if customer.money < cheapest_shop_cost:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheapest_shop['name']}")
            customer_home_location = customer.location
            customer.location = cheapest_shop["location"]

            print("\nDate: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")

            print(f"{customer.product_cart['milk']} milks "
                  f"for {cheapest_shop['milk_money']} dollars")
            print(f"{customer.product_cart['bread']} breads "
                  f"for {cheapest_shop['bread_money']} dollars")
            print(f"{customer.product_cart['butter']} butters "
                  f"for {cheapest_shop['butter_money']} dollars")
            print(f"Total cost is {cheapest_shop['products_money']} dollars")
            print("See you again!")

            print(f"\n{customer.name} rides home")
            customer.location = customer_home_location

            money_left = customer.money - cheapest_shop["final_cost"]

            print(f"{customer.name} now has {money_left} dollars\n")
