from app.car import Car
from app.customer import Customer
from app.shop import Shop


def total_costs(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> float | int:
    cost = 0
    trip_cost = customer.car.cost_ride(
        customer.location, shop.location, fuel_price)
    for key, value in customer.product_cart.items():
        cost += shop.products[key] * value
    total_cost = round(trip_cost + cost, 2)
    return total_cost


def customers_registration(customers_data: dict) -> list[Customer]:
    customers = []
    for customer in customers_data:
        car = Car(customer["car"]["brand"],
                  customer["car"]["fuel_consumption"])
        client = Customer(customer["name"],
                          customer["product_cart"],
                          customer["location"],
                          customer["money"], car)
        customers.append(client)
    return customers


def shop_registration(shops_data: dict) -> list[Shop]:
    shops = []
    for shop in shops_data:
        new_shop = Shop(shop["name"], shop["location"], shop["products"])
        shops.append(new_shop)
    return shops
