import json

from app.customers import Customer


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        data = json.load(file)
    bob = Customer(data["customers"][0]["name"],
                   data["customers"][0]["product_cart"],
                   data["customers"][0]["location"],
                   data["customers"][0]["money"],
                   data["customers"][0]["car"])

    alex = Customer(data["customers"][1]["name"],
                    data["customers"][1]["product_cart"],
                    data["customers"][1]["location"],
                    data["customers"][1]["money"],
                    data["customers"][1]["car"])

    monica = Customer(data["customers"][2]["name"],
                      data["customers"][2]["product_cart"],
                      data["customers"][2]["location"],
                      data["customers"][2]["money"],
                      data["customers"][2]["car"])
    bob.print()
    alex.print()
    monica.print()
