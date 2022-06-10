from customer.customer import Customer
from json_unit.json_unit import JSONData
from shop.shop import Shop


def shop_trip():
    all_data = JSONData("config.json")
    customers_list = [Customer(field) for field in all_data.data["customers"]]
    shop_list = [Shop(field) for field in all_data.data["shops"]]
    for customer in customers_list:
        customer_has_money = customer.show_me_costumers_money()
        print(customer_has_money[0])
        trip_list = [
            customer.cost_shopping_trip(shop, all_data.data["FUEL_PRICE"]) for
            shop in shop_list]
        for trip in trip_list:
            print(trip[0])
        trip_list = sorted(trip_list, key=lambda i: i[1])
        if trip_list[0][1] <= customer_has_money[1]:
            print(customer.direction_to_ride(trip_list[0][3]))
            print(trip_list[0][3].print_a_bill(customer,
                                               all_data.data["FUEL_PRICE"]))
            print(customer.direction_to_ride())
            print(customer.show_me_costumers_money(" now")[0])
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")

# shop_trip()
