from json import load


class JSONData:
    def __init__(self, file_name: str):
        with open(file_name) as f:
            self.data = load(f)
