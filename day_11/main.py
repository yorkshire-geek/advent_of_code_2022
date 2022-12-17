from utils.objectmother import ObjectMother
from monkey import Monkey
from monkey import MonkeyDataWrapper
from functools import reduce


def play_single_round(round_number: int):
    for monkey in monkeys:
        while monkey.items:
            monkey_index, worry_level = monkey.inspect_item()
            monkeys[monkey_index].receive_item(worry_level)
        print("Round ", round_number+1, [monkey for monkey in monkeys])


if __name__ == "__main__":
    monkeys_data = ObjectMother("input.txt").return_list_of_multi_line_objects(MonkeyDataWrapper.factory, "Monkey")

    monkeys = []
    for monkey_data in monkeys_data:
        monkeys.append(Monkey(monkey_data.get_name(), monkey_data.get_starting_items(), monkey_data.get_operation(), monkey_data.get_test()))

    divisors = [monkey.get_divisor() for monkey in monkeys]
    Monkey._modulo = reduce(lambda x, y: x * y, divisors)

    for n in range(10000):
        play_single_round(n)

    sorted_list = sorted([monkey.get_inspected() for monkey in monkeys])
    print(sorted_list)
    print("ans: ", sorted_list[-1] * sorted_list[-2])
