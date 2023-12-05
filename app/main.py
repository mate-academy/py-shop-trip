import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)
        customers = data.get("customers")
        shops = data.get("shops")
        fuel_cost = data.get("FUEL_PRICE")

    def create_customer_object(customers: dict) -> list:
        for customer in customers:
            customer["name"] = Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]
            )
        return Customer.instances

    def create_shop_object(shops: dict) -> list:
        for shop in shops:
            shop["name"] = Shop(
                shop["name"],
                shop["products"],
                shop["location"]
            )
        return Shop.instances
    customer_dict = create_customer_object(customers)
    create_shop_object(shops)
    for customer in customer_dict:
        print(f"{customer.name} has {customer.money} dollars")
        groceries = customer.groceries_cost()
        cost = customer.road_cost(fuel_cost)
        for key, value in cost.items():
            cost[key] = cost[key] + groceries[key]["total_cost"]
            print(f"{customer.name}'s trip to the "
                  f"{key} costs {cost[key]}")
        preferable_shop = min(cost.items(), key=lambda x: x[1])
        if customer.money < preferable_shop[1]:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {preferable_shop[0]}\n")
        customer.get_receipt(groceries, preferable_shop)
        customer.get_home()
