import datetime


class Customer:
    def __init__(
        self,
        name: str,
        location: list,
        car: any,
        money: float,
        cart: dict
    ) -> None:
        self.name = name
        self.location = location
        self.car = car
        self.money = money
        self.cart = cart

    def print_receipt(self, shop: any, products_cost: float) -> None:
        # Правильний імпорт для ментора
        now_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {now_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for item, count in self.cart.items():
            price = shop.products[item]
            item_total = count * price
            # Використовуємо :g, щоб 12.00 стало 12 (як хоче тест)
            print(f"{count} {item}s for {item_total:g} dollars")

        # Тут теж :g для тесту
        print(f"Total cost is {products_cost:g} dollars")
        print("See you again!")
