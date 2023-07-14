import datetime


class Shop:
    def __init__(self, name, location, products):
        self.print_receipt()

    def print_receipt(self):
        print(datetime.datetime.now())


if __name__ == '__main__':
    x = Shop(name="", location="", products="")
