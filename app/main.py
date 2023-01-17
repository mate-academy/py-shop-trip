from app.shop import Shop
from app.customers import Customer


def shop_trip() -> None:
    shops_list = Shop.create_class_instance_shops_list()
    customers_list = Customer.create_class_instance_customers_list()

    for customer in customers_list:
        shops_cost = []
        shops = []

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops_list:
            shop_dict = shop.create_shop_dict(customer)

            shops.append(shop_dict)
            shops_cost.append(shop_dict["final_cost"])

            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {shop_dict['final_cost']}")

        cheapest_shop = Shop.find_cheapest_shop(shops_cost, shops)

        customer.make_prints_for_shop_visit(cheapest_shop)
