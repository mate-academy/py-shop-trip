from app.customers import customers


def shop_trip():
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop, cheapest_trip = customer.find_cheapest_shop()
        if cheapest_trip > customer.money:
            print(f"{customer.name} doesn't have enough"
                  f" money to make purchase in any shop")
            continue
        customer.go_to_cheapest_shop(cheapest_shop, cheapest_trip)
        customer.go_home()


if __name__ == "__main__":
    shop_trip()
