import datetime
from app.customer import customer_class
from app.trip_cost import trip_cost
from app.shop import shop_class


def shop_trip() -> None:
    for customer in customer_class:
        index_customer = customer_class.index(customer)
        cost_customer = []
        print(f"{customer.name} has {customer.money} dollars")
        for index in range(index_customer * 3, (index_customer + 1) * 3):
            print(f"{customer.name}'s trip to the "
                  f"{shop_class[index % 3].name} costs {trip_cost[index]}")

            cost_customer.append(trip_cost[index])

        min_cost = min(cost_customer)

        if min_cost <= customer.money:
            print(f"{customer.name} rides to "
                  f"{shop_class[cost_customer.index(min_cost)].name}\n")

            today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {today}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")
            milk = (customer.product_cart["milk"]
                    * shop_class[cost_customer.index(min_cost)]
                    .products["milk"])
            bread = (customer.product_cart["bread"]
                     * shop_class[cost_customer.index(min_cost)]
                     .products["bread"])
            butter = (customer.product_cart["butter"]
                      * shop_class[cost_customer.index(min_cost)]
                      .products["butter"])
            print(f"{customer.product_cart['milk']} milks for "
                  f"{milk} dollars")
            print(f"{customer.product_cart['bread']} breads for "
                  f"{bread} dollars")
            print(f"{customer.product_cart['butter']} butters for "
                  f"{butter} dollars")
            print(f"Total cost is {milk + bread + butter} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min_cost} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


shop_trip()
