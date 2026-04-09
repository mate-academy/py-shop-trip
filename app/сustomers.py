class Customers:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def ride_to_shop(self, coord_s: list) -> None:
        self.home = self.location
        self.location = coord_s

    def ride_home(self) -> None:
        self.location = self.home


def create_customers(list_customers: list[Customers]) -> dict:
    customers = {}
    for customer in list_customers:
        customers[customer["name"]] = Customers(customer["name"],
                                                customer["product_cart"],
                                                customer["location"],
                                                customer["money"],
                                                customer["car"])
    return customers
