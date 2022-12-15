from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper


class MonkeyDataWrapper (DataWrapper):
    @staticmethod
    def factory(data):
        return DataWrapper(data)

    def get_command(self) -> int:
        return self.data.split(" ")[0]

    def get_value(self) -> int:
        return int(self.data.split(" ")[1])


if __name__ == "__main__":
    monkeys = ObjectMother("input_test.txt").return_list(MonkeyDataWrapper.factory)
