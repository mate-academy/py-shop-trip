import json
from app.customer import Customer
from app.shop import Shop
from app.cost_calculation import Cost_Calculation


def shop_trip():
    data = None
    customers = []  # Customer obj
    shops = []  # Shop obj
    results = {}

    # Func where customers calculate how much will
    # cost trip for the products in every shop
    # and pick the cheapest one and ride there if they have enough money.

    # When the customer arrives at the shop his location
    # should equal to shop location.

    # After customer buys products,
    # shop prints purchase receipt using current time

    # The cost of the trip consists of three parts:
    # the fuel cost to get to the shop,
    # cost of all products to buy,
    # the fuel cost to get home.

    # After the shop he arrives home and counts the remaining money.

    data = None  # TODO: get and sort data
    source = "config.json"
    try:
        with open(source, "r") as file:  # read
            data = json.load(file)
    except Exception as e:
        print(e)
    sorted_data = []
    print(data)
    for _ in sorted_data:
        pass
    Customer(name="test_name",
             product_cart=".",
             location="",
             money="",
             car=""
             )
    Shop(
        name="",
        location="",
        products=""
    )
    for customer in customers:
        for shop in shops:
            cost = Cost_Calculation.calculation(customer, shop)
            results = {
                customer: {
                    shop: cost
                },
            }


if __name__ == "__main__":
    shop_trip()
