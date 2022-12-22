from collections import deque
import string
import networkx as nx

LETTERS_A_TO_Z = string.ascii_lowercase


def find_char(collection: (), char_to_find: chr) -> ():
    for r, row in enumerate(collection):
        if char_to_find in row:
            c = row.index(char_to_find)
            break
    return r, c


def char_replace(collection: (), char_from: chr, char_to: chr):
    for n, jobber in enumerate(collection):
        if char_from in jobber:
            collection[n] = jobber.replace(char_from, char_to)


# Graph comes in the format [row][col]
# so 2 rows, 3 cols
#   abc
#   def
# grid[0][0] = d, grid[0][1] = e, grid[0][2] = f,  grid[1][0] = a, grid[1][1] = b, grid[1][2] = c
#
def setup_graphs(grid: ()):

    rows = len(grid)
    cols = len(grid[0])

    start = find_char(grid, 'S')
    end = find_char(grid, 'E')

    char_replace(grid, 'S', 'a')
    char_replace(grid, 'E', 'z')

    # visited = [[False for _ in range(cols)] for _ in range(rows)]

    print(grid)
    graph = nx.DiGraph()
    for row in range(rows):
        for col in range(cols):
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < rows and 0 <= c < cols:
                    source_height = LETTERS_A_TO_Z.index(grid[row][col])
                    destination_height = LETTERS_A_TO_Z.index(grid[r][c]) - 1
                    if destination_height <= source_height:
                        graph.add_edge((row, col), (r, c))

    print(graph)
    jobber = nx.shortest_path(graph, start, end)
    print(jobber)
    print(len(jobber))

#             if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:

    #
    # # Initialize the queue with the starting node
    # queue = deque([start])
    # visited[start[0]][start[1]] = True
    #
    # # Initialize the number of steps to 0
    # steps = 0
    #
    # # BFS loop
    # while queue:
    #     # Increment the number of steps
    #     steps += 1
    #
    #     # Process all the nodes in the current depth level
    #     for _ in range(len(queue)):
    #         row, col = queue.popleft()
    #
    #         # Check if the node is the goal
    #         if grid[row][col] == 'E':
    #             return steps
    #
    #         # Add the unvisited neighbors of the node to the queue
    #         for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
    #             if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
    #                 a = letters_a_to_z.index(grid[r][c])
    #                 b = letters_a_to_z.index(grid[row][col]) + 1
    #                 if a <= b:
    #                     queue.append((r, c))
    #                     visited[r][c] = True
    #
    # # Return -1 if the goal is not reached
    # return -1


if __name__ == "__main__":

    with open("input.txt", "r") as filename:
        input_grid = filename.read().splitlines()

    setup_graphs(input_grid[::-1])


# Here is one way you could find the x, y coordinates of the character E in the given collection:
#
# Copy code
# collection = ['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi']
#
# for y, row in enumerate(collection):
#     if 'E' in row:
#         x = row.index('E')
#         break
#
# print(f"The character E is located at x = {x}, y = {y}")