import datetime


class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def sale_of_goods(self):
        pass

    @staticmethod
    def print_receipt():
        print(datetime.datetime.now())

    def __repr__(self):
        return (
            f"{self.name}, {self.location}, {self.products}"
        )


if __name__ == '__main__':
    x = Shop(name="", location="", products="")
