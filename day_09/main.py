from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper
import copy


class DataWrapper (DataWrapper):
    @staticmethod
    def factory(data):
        return DataWrapper(data)

    def get_direction(self) -> int:
        return self.data.split(" ")[0]

    def get_vector(self) -> int:
        return int(self.data.split(" ")[1])


class Position(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'P(%s, %d)' % (self._x, self._y)

    def __eq__(self, other):
        if isinstance(other, Position):
            return (self._x == other._x) and (self._y == other._y)
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_xy(self) -> ():
        return self._x, self._y

    def move_x(self, step: int):
        self._x += step

    def move_y(self, step: int):
        self._y += step


def process_command(cmd: DataWrapper) -> None:

    match cmd.get_direction():
        case "R":
            move_right_or_left(cmd.get_vector(), 1)
        case "U":
            move_up_or_down(cmd.get_vector(), 1)
        case "L":
            move_right_or_left(cmd.get_vector(), -1)
        case "D":
            move_up_or_down(cmd.get_vector(), -1)
        case _:
            print("command not found: ", cmd.get_direction())


def move_right_or_left(magnitude: int, direction: int) -> None:
    for n in range(0, magnitude):
        head_position.move_x(direction)
        move_tails()


def move_up_or_down(magnitude: int, direction: int) -> None:
    for n in range(0, magnitude):
        head_position.move_y(direction)
        move_tails()


def move_tails():
    move_tail(head_position, tail_positions[0])
    for n in range(1, TAIL_SIZE):
        move_tail(tail_positions[n-1], tail_positions[n])

    if tail_trail[-1] != tail_positions[-1]:
        tail_trail.append(copy.copy(tail_positions[-1]))


def move_tail(head: Position, tail: Position) -> None:
    # right or left
    if abs(head.get_x() - tail.get_x()) > 1:
        if abs(head.get_y() - tail.get_y()) > 0:
            tail.move_y(1 if head.get_y() > tail.get_y() else -1)  # adjust for diagonals
        tail.move_x(1 if head.get_x() > tail.get_x() else -1)

    # up or down
    if abs(head.get_y() - tail.get_y()) > 1:
        if abs(head.get_x() - tail.get_x()) > 0:
            tail.move_x(1 if head.get_x() > tail.get_x() else -1)  # adjust for diagonals
        tail.move_y(1 if head.get_y() > tail.get_y() else -1)


def print_board() -> None:
    min_x = -12
    min_y = -1
    max_x = 16
    max_y = 16

    for y in range(max_y, min_y, -1):
        print()
        for x in range(min_x, max_x):
            display_char = "."
            if Position(0, 0) == Position(x, y):
                display_char = "s"

            if head_position == Position(x, y):
                display_char = "H"
            else:
                for index in range(TAIL_SIZE):
                    if tail_positions[index] == Position(x, y):
                        display_char = str(index + 1)
                        break

            print(display_char, end="")


if __name__ == "__main__":
    TAIL_SIZE = 9
    tail_positions = [Position(0, 0) for i in range(TAIL_SIZE)]
    head_position = Position(0, 0)

    tail_trail = [copy.copy(tail_positions[-1])]

    commands = ObjectMother("input.txt").return_list(DataWrapper.factory)

    for command in commands:
        process_command(command)

    print("answer: ", len(set(tail_trail)))

    # print("tail positions:", tail_positions)
    # print("head position: ", head_position)
    # print_board()
