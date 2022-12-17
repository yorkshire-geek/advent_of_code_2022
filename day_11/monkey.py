import operator
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
        return self.data[3] + " " + self.data[4] + " " + self.data[5]


class Monkey:
    _modulo = -1  # 9699690

    def __init__(self, name: str, items: [], operation_str: str, test: str):
        self.name = name
        self.items = [int(x) for x in items]
        self.operation_str = operation_str
        self.test = test
        self._divisor = int(self.test.split(" ")[3])
        self.monkey_if_true = int(self.get_test().split(" ")[9])
        self.monkey_if_false = int(self.get_test().split(" ")[15])
        self.inspected = 0

    def __repr__(self):
        return self.name + str(self.items) + " i:" + str(self.inspected)

    def get_name(self):
        return self.name

    def get_items(self):
        return self.items

    def get_operation_str(self):
        return self.operation_str

    def get_inspected(self):
        return self.inspected

    def get_test(self):
        return self.test

    def get_divisor(self):
        return self._divisor

    def get_operator_function(self):
        result = operator.mul
        if "+" in self.operation_str:
            result = operator.add
        return result

    def get_new_worry_level(self, old_worry_level: int) -> int:
        result = self.get_operator_function()(old_worry_level, self.get_param(old_worry_level))
        result = result % Monkey._modulo
        return result

    def get_param(self, worry_level:int) -> int:
        param = self.get_operation_str().split(" ")[4]
        if param == "old":
            param = worry_level

        return int(param)

    def inspect_item(self) -> (int, int):
        self.inspected += 1
        new_worry = self.get_new_worry_level(self.items.pop(0))
        # new_worry //= 3 # part one
        return self.get_monkey_to_throw_to(new_worry), new_worry

    def get_monkey_to_throw_to(self, worry_level):
        if worry_level % self._divisor == 0:
            return int(self.get_test().split(" ")[9])
        else:
            return int(self.get_test().split(" ")[15])

    def receive_item(self, worry_level):
        self.items.append(worry_level)




