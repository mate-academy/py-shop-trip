from app.shop import create_class_instance_shops_list, \
    create_shop_dict, find_cheapest_shop
from app.customers import create_class_instance_customers_list, \
    make_rest_of_prints


def shop_trip() -> None:
    shops_list = create_class_instance_shops_list()
    customers_list = create_class_instance_customers_list()

    for customer in customers_list:
        shops_cost = []
        shops = []

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops_list:
            shop_dict = create_shop_dict(customer, shop)

            shops.append(shop_dict)
            shops_cost.append(shop_dict["final_cost"])

            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {shop_dict['final_cost']}")

        cheapest_shop = find_cheapest_shop(shops_cost, shops)

        make_rest_of_prints(customer, cheapest_shop)
