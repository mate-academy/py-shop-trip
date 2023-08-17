import datetime
from app.customer import create_customers
from app.trip_cost import trip_cost
from app.shop import create_shops


def shop_trip() -> None:
    customer_class = create_customers()
    cost_of_trip = trip_cost()
    shop_class = create_shops()
    for customer in customer_class:
        index_customer = customer_class.index(customer)
        cost_customer = []
        print(f"{customer.name} has {customer.money} dollars")
        for index in range(index_customer * 3, (index_customer + 1) * 3):
            print(f"{customer.name}'s trip to the "
                  f"{shop_class[index % 3].name} costs {cost_of_trip[index]}")

            cost_customer.append(cost_of_trip[index])

        min_cost = min(cost_customer)

        if min_cost <= customer.money:
            print(f"{customer.name} rides to "
                  f"{shop_class[cost_customer.index(min_cost)].name}\n")

            today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {today}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")

            total = 0
            for product in customer.product_cart:
                cost = (customer.product_cart[product]
                        * shop_class[cost_customer.index(min_cost)]
                        .products[product])
                print(f"{customer.product_cart[product]} {product}s for "
                      f"{cost} dollars")
                total += cost

            print(f"Total cost is {total} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min_cost} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
