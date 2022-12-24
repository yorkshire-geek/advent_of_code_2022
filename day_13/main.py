def test(left: str, right: str) -> bool:
    index = 0

    return False


if __name__ == "__main__":
    with open("input_test.txt", "r") as filename:
        lines = filename.read().split("\n\n")

    # for jobber in
    # for left, right  in lines.split()§

    items = [[line.split("\n")[0], line.split("\n")[1]] for line in lines]

    item = items[0]
    print("", item, test(item[0], item[1]))


