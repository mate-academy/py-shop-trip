from datetime import datetime
from app import methods


def shop_trip():
    customers = methods.CUSTOMERS
    shops = methods.SHOPS

    for customer in customers:
        list_cost = methods.cost_products_list(customer, shops)
        travel_cost = methods.cost_get_to_shop(customer, shops)
        home_coordinats = customer["location"]
        print(f"{customer['name']} has {customer['money']} dollars")
        choice = methods.make_choice(customer, shops)

        if choice is None:
            print(f"{customer['name']} doesn't have enough money "
                  f"to make purchase in any shop")
            continue

        print(f"{customer['name']} rides to {choice}")
        customer["location"] = [shop["location"]
                                for shop in shops if shop["name"] == choice]
        print()
        print(f"Date: {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")
        print(f"Thanks, {customer['name']}, for you purchase!")
        print("You have bought: ")
        for product in customer["product_cart"]:
            print(f"{customer['product_cart'][product]} {product}s "
                  f"for {list_cost[choice][1][product]} dollars")
        print(f"Total cost is {list_cost[choice][0]} dollars")
        print("See you again!")
        print()
        print(f"{customer['name']} rides home")
        customer["location"] = home_coordinats
        customer["money"] -= (list_cost[choice][0] + travel_cost[choice])
        print(f"{customer['name']} now has {customer['money']} dollars")
        print()


if __name__ == "__main__":
    shop_trip()
