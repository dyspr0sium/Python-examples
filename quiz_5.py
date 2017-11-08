# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by Daniel Yang and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():
    paths = defaultdict(int)
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                for e in get_path_length_from(i,j):
                    paths[e] += 1
    return paths

def get_path_length_from(i,j):

    N = get_path_length_from(i-1, j) if i and grid[i-1][j] == grid[i][j] + 1 else []
    S = get_path_length_from(i+1, j) if i < height - 1 and grid[i+1][j] == grid[i][j] + 1 else []
    W = get_path_length_from(i, j-1) if j and grid[i][j-1] == grid[i][j] + 1 else []
    E = get_path_length_from(i, j+1) if j < width - 1 and grid[i][j+1] == grid[i][j] + 1 else []
    
    if all(not e for e in [N, S, W, E]):
        return [1]
    return [x+1 for x in N + S + W + E]

try:
    for_seed, max_length, height, width = [int(i) for i in input('Enter four nonnegative integers: ').split()]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')