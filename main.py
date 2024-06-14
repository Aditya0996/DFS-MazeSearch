from collections import deque
from random import randint
from timeit import default_timer as timer

# to keep track of the blocks of maze
class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# each block will have its own position and cost of steps taken
class Node1:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost


def create_node(x, y, c):
    val = Grid_Position(x, y)
    return Node1(val, c + 1)


# dfs algo for maze
def dfs(Grid, dest: Grid_Position, start: Grid_Position, blocks):
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]
    m, n = (len(Grid), len(Grid))
    visited_blocks = blocks

    visited_blocks[start.x][start.y] = True
    stack1 = deque()
    sol = Node1(start, 0)
    stack1.append(sol)
    neigh = 4
    cost = 0
    while stack1:
        current_block = stack1.pop()
        current_pos = current_block.pos
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algorithm used = DFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return current_block.cost
        x_pos = current_pos.x
        y_pos = current_pos.y

        for i in range(neigh):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos != m and x_pos != -1 and y_pos != n and y_pos != -1:
                if Grid[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        cost += 1
                        visited_blocks[x_pos][y_pos] = True
                        stack1.append(create_node(x_pos, y_pos, current_block.cost))
    return -1


# Class to define structure of a node
class Node:
    def __init__(self, value=None,
                 next_element=None):
        self.val = value
        self.next = next_element


# Class to implement a stack
class stack:

    # Constructor
    def __init__(self):
        self.head = None
        self.length = 0

    # Put an item on the top of the stack
    def insert(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    # Return the top position of the stack
    def pop(self):
        if self.length == 0:
            return None
        else:
            returned = self.head.val
            self.head = self.head.next
            self.length -= 1
            return returned

    # Return False if the stack is empty
    # and true otherwise
    def not_empty(self):
        return bool(self.length)

    # Return the top position of the stack
    def top(self):
        return self.head.val


# Function to generate the random maze
def random_maze_generator(r, c, P0, Pf):
    ROWS, COLS = r, c

    # Array with only walls (where paths will
    # be created)
    maze = list(list(0 for _ in range(COLS))
                for _ in range(ROWS))

    # Auxiliary matrices to avoid cycles
    seen = list(list(False for _ in range(COLS))
                for _ in range(ROWS))
    previous = list(list((-1, -1)
                         for _ in range(COLS)) for _ in range(ROWS))

    S = stack()

    # Insert initial position
    S.insert(P0)

    # Keep walking on the graph using dfs
    # until we have no more paths to traverse
    # (create)
    while S.not_empty():

        # Remove the position of the Stack
        # and mark it as seen
        x, y = S.pop()
        seen[x][y] = True

        # Check if it will create a cycle
        # if the adjacent position is valid
        # (is in the maze) and the position
        # is not already marked as a path
        # (was traversed during the dfs) and
        # this position is not the one before it
        # in the dfs path it means that
        # the current position must not be marked.

        # This is to avoid cycles with adj positions
        if (x + 1 < ROWS) and maze[x + 1][y] == 1 \
                and previous[x][y] != (x + 1, y):
            continue
        if (0 < x) and maze[x - 1][y] == 1 \
                and previous[x][y] != (x - 1, y):
            continue
        if (y + 1 < COLS) and maze[x][y + 1] == 1 \
                and previous[x][y] != (x, y + 1):
            continue
        if (y > 0) and maze[x][y - 1] == 1 \
                and previous[x][y] != (x, y - 1):
            continue

        # Mark as walkable position
        maze[x][y] = 1

        # Array to shuffle neighbours before
        # insertion
        to_stack = []

        # Before inserting any position,
        # check if it is in the boundaries of
        # the maze
        # and if it were seen (to avoid cycles)

        # If adj position is valid and was not seen yet
        if (x + 1 < ROWS) and seen[x + 1][y] == False:
            # Mark the adj position as seen
            seen[x + 1][y] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x + 1, y))

            # Memorize the current position as its
            # previous position on the path
            previous[x + 1][y] = (x, y)

        if (0 < x) and seen[x - 1][y] == False:
            # Mark the adj position as seen
            seen[x - 1][y] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x - 1, y))

            # Memorize the current position as its
            # previous position on the path
            previous[x - 1][y] = (x, y)

        if (y + 1 < COLS) and seen[x][y + 1] == False:
            # Mark the adj position as seen
            seen[x][y + 1] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x, y + 1))

            # Memorize the current position as its
            # previous position on the path
            previous[x][y + 1] = (x, y)

        if (y > 0) and seen[x][y - 1] == False:
            # Mark the adj position as seen
            seen[x][y - 1] = True

            # Memorize the position to insert the
            # position in the stack
            to_stack.append((x, y - 1))

            # Memorize the current position as its
            # previous position on the path
            previous[x][y - 1] = (x, y)

        # Indicates if Pf is a neighbour position
        pf_flag = False
        while len(to_stack):

            # Remove random position
            neighbour = to_stack.pop(randint(0, len(to_stack) - 1))

            # Is the final position,
            # remember that by marking the flag
            if neighbour == Pf:
                pf_flag = True

            # Put on the top of the stack
            else:
                S.insert(neighbour)

        # This way, Pf will be on the top
        if pf_flag:
            S.insert(Pf)

    # Mark the initial position
    x0, y0 = P0
    xf, yf = Pf
    maze[x0][y0] = 1
    maze[xf][yf] = 1

    # Return maze formed by the traversed path
    return maze


def main():
    N = 5
    M = N
    x_start = 0
    y_start = 0
    x_end = N-2
    y_end = M-1

    P0 = (x_start, y_start)
    P1 = (x_end, y_end)
    maze = random_maze_generator(N, M, P0, P1)
    for x in range(len(maze)):
        print(maze[x])
    destination = Grid_Position(x_start, y_start)
    starting_position = Grid_Position(x_end, y_end)
    blocks = [[False for i in range(M)]
                      for j in range(N)]
    start = timer()
    res2 = dfs(maze, destination, starting_position, blocks)
    if res2 != -1:
        print("Steps with backtracking = ", res2)
    else:
        print("Path does not exit")
    end = timer()
    print((end - start)*1000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
