from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper

accumulator = 0
cycle = 0
x = 1
future_buffer = {}
pixels = []


class DataWrapper (DataWrapper):
    @staticmethod
    def factory(data):
        return DataWrapper(data)

    def get_command(self) -> int:
        return self.data.split(" ")[0]

    def get_value(self) -> int:
        return int(self.data.split(" ")[1])


def update_cycle():
    global accumulator, cycle, x

    # End of Cycle
    if cycle in future_buffer:
        x += future_buffer[cycle]

    # start of Cycle
    cycle += 1

    if cycle in (x-2, x-1, x, x+1):
        pixels.append("#")
    else:
        pixels.append(".")

    if cycle in [20, 60, 100, 140, 180, 220]:
        accumulator += (cycle * x)
        print_state()


def process_command(cmd: DataWrapper) -> None:
    # global cycle
    # global x, accumulator

    match cmd.get_command():
        case "noop":
            pass
        case "addx":
            future_buffer[cycle + 2] = cmd.get_value()
            process_command(DataWrapper("noop"))

        case _:
            print("Undefined command: ", cmd.get_command())

    update_cycle()


def print_state() -> None:
    print("cycle[", cycle, "] x = ", x, "strength: ", cycle * x, "accumulator: ", accumulator)


def print_pixels() -> None:
    for n in range(0, 6):
        print("")
        for m in range(0, 40):
            index = (n * 40) + m
            print(pixels[index], end="")


if __name__ == "__main__":
    commands = ObjectMother("input_test_2.txt").return_list(DataWrapper.factory)

    for command in commands:
        process_command(command)

    print("answer: ", accumulator)

    print(future_buffer)
    print_pixels()
