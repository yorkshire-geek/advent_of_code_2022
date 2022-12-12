width = 0
height = 0


def setup_commands(filename: str) -> []:
    result = {}

    with open(filename) as file:
        lines = file.read().splitlines()
        lines.reverse()
        for y in range(0, len(lines)):
            line = lines[y]
            for x in range(0, len(line)):
                result[(x+1, y+1)] = line[x]

    return result, x+1, y+1


def check(result: {}, x: int, y: int) -> None:
    # checkUp
    visible_up = True
    for up in range(y+1, height+1):
        if tree_dict[(x, up)] >= tree_dict[(x, y)]:
            visible_up = False
            break

    # checkDown
    visible_down = True
    for down in range(1, y):
        if tree_dict[(x, down)] >= tree_dict[(x, y)]:
            visible_down = False
            break

    # checkLeft
    visible_left = True
    for left in range(1, x):
        if tree_dict[(left, y)] >= tree_dict[(x, y)]:
            visible_left = False
            break

    # checkRight
    visible_right = True
    for right in range(x+1, width+1):
        if tree_dict[(right, y)] >= tree_dict[(x, y)]:
            visible_right = False
            break

    if visible_up or visible_down or visible_left or visible_right:
        result[(x, y)] = calculate_score(x,y)


def calculate_score(x:int, y:int) -> int:
    score_up = 0
    for up in range(y+1, height+1):
        score_up += 1
        if tree_dict[(x, up)] >= tree_dict[(x, y)]:
            break


    score_down = 0
    for down in range(1, y):
        score_down += 1
        if tree_dict[(x, down)] >= tree_dict[(x, y)]:
            break


    # checkLeft
    score_left = 0
    for left in range(1, x):
        score_left += 1
        if tree_dict[(left, y)] >= tree_dict[(x, y)]:
            break

    score_right = 0
    for right in range(x + 1, width + 1):
        score_right += 1
        if tree_dict[(right, y)] >= tree_dict[(x, y)]:
            break

    return score_up * score_down * score_left * score_right


if __name__ == "__main__":
    tree_dict, width, height = setup_commands('input.txt')
    result_dict = {}

    print(tree_dict)
    print("w:", width)
    print("h:", height)

    for x in range(2, width):
        for y in range(2, height):
            check(result_dict, x, y)

    # check(result_dict, 3, 2)
    print(result_dict)

    values_in_order = sorted(result_dict.values())

    print("answer:", len(result_dict) + (width-1)*2 + (height-1)*2)
    print(values_in_order)


