# From Chat GPT
#
# To solve this problem, you can use a search algorithm such as breadth-first search (BFS). BFS is an algorithm that allows you to explore the nodes of a graph in a breadth-first manner, meaning that it visits all the nodes at a given depth level before moving on to the next depth level.
# Here's how you can apply BFS to solve this problem:
# Create a queue to store the nodes that need to be visited. Initially, the queue should contain only the starting node (S).
# While the queue is not empty, do the following:
# Pop the first node from the queue and mark it as visited.
# If the node is the goal (E), return the number of steps it took to reach the goal.
# Otherwise, add the unvisited neighbors of the node to the queue. The neighbors should be added in the order up, down, left, right.
# If the goal is not reached, return -1 to indicate that it is not possible to reach the goal.
# Here's some example code in Python that implements the above approach:
#
#
from collections import deque


def fewest_steps(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    # Create a 2D array to keep track of visited nodes
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Initialize the queue with the starting node
    queue = deque([start])
    visited[start[0]][start[1]] = True

    # Initialize the number of steps to 0
    steps = 0

    # BFS loop
    while queue:
        # Increment the number of steps
        steps += 1

        # Process all the nodes in the current depth level
        for _ in range(len(queue)):
            row, col = queue.popleft()

            # Check if the node is the goal
            if grid[row][col] == 'E':
                return steps

            # Add the unvisited neighbors of the node to the queue
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and grid[r][c] != '#':
                    queue.append((r, c))
                    visited[r][c] = True

    # Return -1 if the goal is not reached
    return -1


if __name__ == "__main__":
    grid = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]
    start = (0, 0)
    goal = (2, 5)

    steps = fewest_steps(grid, start, goal)
    print(steps)