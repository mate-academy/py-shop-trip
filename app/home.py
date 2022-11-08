class Home:
    homes = {}

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Home.homes[self.name] = self.location
