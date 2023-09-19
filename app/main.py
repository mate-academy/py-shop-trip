from app.customers import Customer


def shop_trip() -> None:

    data = Customer.get_data()
    customers = []

    for customer_data in data["customers"]:
        customer = Customer(customer_data["name"],
                            customer_data["product_cart"],
                            customer_data["location"],
                            customer_data["money"],
                            customer_data["car"])
        customers.append(customer)

    customers[0].user_go_to_shopping()
    customers[1].user_go_to_shopping()
    customers[2].user_go_to_shopping()
