from utils.objectmother import ObjectMother
from monkey import Monkey
from monkey import MonkeyDataWrapper


if __name__ == "__main__":
    monkeys_data = ObjectMother("input_test.txt").return_list_of_multi_line_objects(MonkeyDataWrapper.factory, "Monkey")

    monkeys = []
    for monkey_data in monkeys_data:
        monkeys.append(Monkey(monkey_data.get_name(), monkey_data.get_starting_items(), monkey_data.get_operation(), monkey_data.get_test()))

    print(monkeys)
    print(monkeys[0].get_operation())
    print(monkeys[0].get_test())

