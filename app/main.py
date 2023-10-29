import app.json_parser
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    data = app.json_parser.read_json_from_file("app/config.json")
    fuel_price = app.json_parser.get_fuel_price(data)

    customers = [
        Customer(customer_data)
        for customer_data
        in app.json_parser.get_customers_data(data)
    ]
    shops = [
        Shop(shop_data)
        for shop_data
        in app.json_parser.get_shops_data(data)
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        possible_shops = customer.calculate_total_trip_cost_for_each_shop(
            shops, fuel_price
        )

        for shop in shops:
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {possible_shops[shop]}")

        cheapest_shop = customer.choose_cheapest_shop()

        if customer.evaluate_shopping_possibility():
            customer.go_to_the_shop()
            print(f"{customer.name} rides to {cheapest_shop['shop'].name}"
                  "\n")

            cheapest_shop["shop"].print_purchase_receipt(customer)

            customer.go_home()
            print(f"{customer.name} rides home")

            rest_of_money = customer.calculate_rest_of_money()
            print(f"{customer.name} now has {rest_of_money} dollars"
                  "\n")

        else:
            print(f"{customer.name} doesn't have enough "
                  "money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
