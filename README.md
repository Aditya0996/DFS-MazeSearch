# Maze Solving using Depth First Search

## Problem
Model a given maze as a graph. Find the target using depth first search. The algorithm should run in linear time. Use the given input sets as tests.

## Problem Analysis
The following assumptions are made :
1. Each maze has only one starting point and an ending point.
2. We also assume that mazes are composed of walls (marked as 0s), these walls will be considered untraversable.
3. We are finding the first available path through the maze.

We structure our maze as a graph with nodes and edges. The visited property defines a way that we can determine if we’ve seen a node already. That way we aren’t traversing over nodes multiple times. Edges are what link nodes together. If there is no edge between two nodes, we go back to our second assumption(mazes have walls) and use no edge as an indication that we can’t traverse in that direction. The basic idea behind all graph traversal techniques is that they visit the node that is “next” in a data structure they maintain (a stack in our case), mark it, and then add its unvisited neighbors to the data structure. The defining characteristic of DFS is that, whenever DFS visits a maze cell (marked as 1), it next searches the sub-maze whose origin is 1 before searching any other part of the maze. This is accomplished by using a Stack to store the
nodes. The end result is that DFS will follow some path through the maze as far as it will go, until a dead end or previously visited location is found. When this occurs, the search backtracks to try another path, until it finds an exit.

## Pseudocode

```plaintext
starting_point = (0, 0)
ending_point = (n-2, n-1)
Maze = Generate random maze of size n x n.
initialize Visited_blocks[n][n] = False
Result = DFS(Maze, ending_point, starting_point)
print(Result)

DFS(Maze, ending_point, starting_point):
    Adjacent_cell_x_axis = [1, 0, 0, -1]
    Adjacent_cell_y_axis = [0, 1, -1, 0]
    m, n = length of grid
    Visited_blocks[starting_point.x][starting_point.y] = True
    Stack.append(Solution)

    While (stack not empty) do:
        current_block = stack.pop()
        current_pos = current_block.pos

        if (current_pos.x == dest.x and current_pos.y == dest.y) then:
            return (current_block.cost)

        x_pos = current_pos.x
        y_pos = current_pos.y

        for (i = 0 to neighbours) do:
            update x_pos, y_pos

            if adjacent cell is present then:
                if not a wall then:
                    if not visited_blocks[x_pos][y_pos] then:
                        cost += 1
                        visited_blocks[x_pos][y_pos] = True
                        stack.append(update stack with (x_pos, y_pos, current_block.cost))
```


## Time Complexity

DFS has a time complexity of O(m + n) , where n is the number of locations you can be in and m is the total number of connections between locations,( n is the number of nodes and m is the number of edges). This is because the algorithm explores each vertex and edge exactly once. For the grid whose size is w × h, then n = wh This means that the runtime will be O(wh).
