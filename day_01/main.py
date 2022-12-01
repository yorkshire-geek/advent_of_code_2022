
if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.read();

    list_of_lists = []
    for x in lines.split('\n\n'):
        list_of_lists.append([int(y) for y in x.splitlines()] )

    list_of_sums = []
    for y in list_of_lists:
        list_of_sums.append(sum(y))


    sorted = sorted(list_of_sums);

    print("answer one: ", max(sorted));
    print("answer two: ", sum(sorted[-3:]))


# import sys

# with open(sys.argv[1], 'r') as f:
#     elves = [x.split('\n') for x in f.read().split("\n\n")]

# cals = sorted([sum([int(x) for x in y if x.isdigit()]) for y in elves])

# print(max(cals))
# print(sum(cals[-3:]))