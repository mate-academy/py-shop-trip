from app.data.json_extraction import customers
from app.objects.customer import Customer
from app.objects.car import Car


customers = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
    )
    for customer in customers
]
