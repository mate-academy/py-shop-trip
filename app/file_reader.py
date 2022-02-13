import ast


def json_reader():
    with open("C:\\Users\\alexg\\Mate\\Projects\\"
              "py-shop-trip\\app\\config.json", "r") as config:
        everything = config.read()
        info = ast.literal_eval(everything)
        return info
