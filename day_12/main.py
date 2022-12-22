import string
import networkx as nx

LETTERS_A_TO_Z = string.ascii_lowercase


def find_all_chars_in_2d_list(input_2d_list: [], char_to_find: chr) -> []:
    result = []
    for row in range(len(input_2d_list)):
        for col in range(len(input_2d_list[0])):
            if input_2d_list[row][col] == char_to_find:
                result.append((row, col))

    return result


def find_char(collection: [], char_to_find: chr) -> ():
    for r, row in enumerate(collection):
        if char_to_find in row:
            c = row.index(char_to_find)
            break
    return r, c


def char_replace(collection: [], char_from: chr, char_to: chr):
    for r, row in enumerate(collection):
        if char_from in row:
            collection[r] = row.replace(char_from, char_to)


# Graph comes in the format [row][col]
# so 2 rows, 3 cols
#   abc
#   def
# grid[0][0] = d, grid[0][1] = e, grid[0][2] = f,  grid[1][0] = a, grid[1][1] = b, grid[1][2] = c
#
def setup_graphs(grid: ()) -> nx.DiGraph:
    rows = len(grid)
    cols = len(grid[0])

    result = nx.DiGraph()
    for row in range(rows):
        for col in range(cols):
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < rows and 0 <= c < cols:
                    source_height = LETTERS_A_TO_Z.index(grid[row][col])
                    destination_height = LETTERS_A_TO_Z.index(grid[r][c]) - 1
                    if destination_height <= source_height:
                        result.add_edge((row, col), (r, c))

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as filename:
        input_grid = filename.read().splitlines()

    input_grid.reverse()

    start = find_char(input_grid, 'S')
    end = find_char(input_grid, 'E')

    char_replace(input_grid, 'S', 'a')
    char_replace(input_grid, 'E', 'z')

    graph = setup_graphs(input_grid)

    print("answer one: ", len(nx.shortest_path(graph, start, end))-1)

    ans_two_dict = {}
    for start_pos in find_all_chars_in_2d_list(input_grid, 'a'):
        try:
            ans_two_dict[start_pos] = len(nx.shortest_path(graph, start_pos, end)) - 1
        except nx.NetworkXNoPath:
            pass

    print(ans_two_dict)
    print(min(ans_two_dict.items(), key=lambda x: x[1]))



