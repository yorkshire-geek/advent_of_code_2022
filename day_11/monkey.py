from utils.datawrapper import DataWrapper


class MonkeyDataWrapper(DataWrapper):
    @staticmethod
    def factory(data):
        return MonkeyDataWrapper(data)

    def get_starting_items(self) -> []:
        return str(self.data[1]).split("Starting items: ")[1].split(", ")

    def get_name(self) -> str:
        return str(self.data[0])

    def get_operation(self) -> str:
        return str(self.data[2]).split("Operation: ")[1]

    def get_test(self) -> str:
        return self.data[3] + self.data[4] + self.data[5]


class Monkey:
    def __init__(self, name: str, items: [], operation: str, test: str):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test

    def get_name(self):
        return self.name

    def get_items(self):
        return self.items

    def get_operation(self):
        return self.operation

    def get_test(self):
        return self.test

    def __repr__(self):
        return self.name + str(self.items)



