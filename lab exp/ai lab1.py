import copy
from heapq import heappush, heappop

n = 3
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

class Node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def calculate_cost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] and mat[i][j] != final[i][j]:
                count += 1
    return count

def print_matrix(mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()
    print()

def is_safe(x, y):
    return 0 <= x < n and 0 <= y < n

def solve(initial, empty_tile_pos, final):
    pq = []
    cost = calculate_cost(initial, final)
    root = Node(None, initial, empty_tile_pos, cost, 0)
    heappush(pq, root)

    while pq:
        minimum = heappop(pq)
        if minimum.cost == 0:
            print_path(minimum)
            return

        for i in range(4):
            new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]
            if is_safe(new_tile_pos[0], new_tile_pos[1]):
                child_mat = copy.deepcopy(minimum.mat)
                # Swap the empty tile
                child_mat[minimum.empty_tile_pos[0]][minimum.empty_tile_pos[1]], child_mat[new_tile_pos[0]][new_tile_pos[1]] = \
                    child_mat[new_tile_pos[0]][new_tile_pos[1]], child_mat[minimum.empty_tile_pos[0]][minimum.empty_tile_pos[1]]
                
                child_cost = calculate_cost(child_mat, final)
                child = Node(minimum, child_mat, new_tile_pos, child_cost, minimum.level + 1)
                heappush(pq, child)

def print_path(root):
    if root is None:
        return
    print_path(root.parent)
    print_matrix(root.mat)

# Example usage
initial = [
    [1, 2, 3],
    [5, 6, 0],
    [7, 8, 4]
]
final = [
    [1, 2, 3],
    [5, 8, 6],
    [0, 7, 4]
]
empty_tile_pos = [1, 2] # Position of '0' in initial matrix
print("Solution Steps:")
solve(initial, empty_tile_pos, final)
