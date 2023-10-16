import app.auxilaries.parsing_shopping as parsing


def shop_trip() -> None:
    _, customers_list, shop_list = parsing.parse_data_from_json()
    customers = parsing.create_customer_classes(customers_list)
    shops = parsing.create_shops_classes(shop_list)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        chosen_shop = parsing.define_destination_shop(customer, shops)
        if chosen_shop:
            customer.visit_shop(chosen_shop)
            customer.get_home(chosen_shop)


if __name__ == "__main__":
    shop_trip()
