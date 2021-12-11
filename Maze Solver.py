import math

import numpy as np
import matplotlib.pyplot as plt

CELL_SIDE = 15
MAX_ENERGY = 250

MAZE_W = 7
MAZE_H = 6

ending_row = 0
ending_col = 0

def make_cell(north, south, east, west):
    cell = np.zeros((CELL_SIDE, CELL_SIDE))

    if north:
        cell[0, :] = -1
    if south:
        cell[CELL_SIDE - 1, :] = -1
    if west:
        cell[:, 0] = -1
    if east:
        cell[:, CELL_SIDE - 1] = -1

    return cell

def set_cell(maze, i, j, cell):
    maze[i * CELL_SIDE : (i + 1) * CELL_SIDE, j * CELL_SIDE : (j + 1) * CELL_SIDE] = cell

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(maze, i, j, value):
  visited.append((i, j))
  queue.append((i, j, value))

  while queue:
    ci, cj, cv = queue.pop(0)
    maze[ci, cj] = cv

    if ci > 0 and maze[ci - 1, cj] >= 0 and (ci - 1, cj) not in visited:
        visited.append((ci-1, cj))
        queue.append((ci-1, cj, cv - 1))

    if ci < (MAZE_H * CELL_SIDE - 1) and maze[ci + 1, cj] >= 0 and (ci + 1, cj) not in visited:
        visited.append((ci+1, cj))
        queue.append((ci+1, cj, cv - 1))

    if cj > 0 and maze[ci, cj - 1] >= 0 and (ci, cj - 1) not in visited:
        visited.append((ci, cj-1))
        queue.append((ci, cj-1, cv - 1))

    if cj < (MAZE_W * CELL_SIDE - 1) and maze[ci, cj + 1] >= 0 and (ci, cj + 1) not in visited:
        visited.append((ci, cj+1))
        queue.append((ci, cj+1, cv - 1))

# def get_gradient(maze, x, y):
#     i = int(x)
#     j = int(y)
#
#     val = maze[i, j]
#
#     if x - i < 0.5:
#
#     else:
#
def gradient_descent(maze, x, y, learning_rate=0.01, threshold=0.001, iterations=220):
    curr_x = x
    curr_y = y

    i = 0

    print(curr_x, curr_y)

    while i < iterations:
        I1 = 0
        I2 = 0
        I3 = 0
        I4 = 0
        I = maze[curr_y, curr_x]

        if curr_x - 1 >= 0 and maze[curr_y, curr_x - 1] != -1:
            I1 = maze[curr_y, curr_x - 1]
        if curr_x + 1 <= (MAZE_W * CELL_SIDE - 1) and maze[curr_y, curr_x + 1] != -1:
            I2 = maze[curr_y, curr_x + 1]
        if curr_y - 1 >= 0 and maze[curr_y - 1, curr_x] != -1:
            I3 = maze[curr_y - 1, curr_x]
        if curr_y + 1 <= (MAZE_H * CELL_SIDE - 1) and maze[curr_y + 1, curr_x] != -1:
            I4 = maze[curr_y + 1, curr_x]

        didx = 0
        if (I1 == 0):
            didx = max(0, I2 - I)
        elif (I2 == 0):
            didx = min(0, I - I1)
        else:
            didx = (I2 - I1) // 2

        didy = 0
        if (I3 == 0):
            didy = max(0, I4 - I)
        elif (I4 == 0):
            didy = min(0, I - I3)
        else:
            didy = (I4 - I3) // 2

        if didx > 0:
            curr_x = int(curr_x + 1)
        if didx < 0:
            curr_x = int(curr_x - 1)

        if didy > 0:
            curr_y = int(curr_y + 1)
        if didy < 0:
            curr_y = int(curr_y - 1)

        #break

        plt.scatter(curr_x, curr_y, color='b', marker='.')
        i += 1

        if (curr_x == ending_col and curr_y == ending_row):
            break

    print(I, I4, I4 - I, didy)


#     while i < iterations:
#         (grad_x, grad_y) = (0, 0) #get_gradient()
#
#         curr_x = prev_x + (learning_rate * grad_x)
#         curr_y = prev_y + (learning_rate * grad_y)
#
#         print(curr_x, curr_y)
#         plt.scatter(curr_x, curr_y, color='r', marker='.')
#
#         if abs(prev_x - curr_x) < threshold and abs(prev_y - curr_y) < threshold:
#             break
#
#         i += 1


def main():
    maze = np.zeros((MAZE_H * CELL_SIDE, MAZE_W * CELL_SIDE))

    set_cell(maze, 0, 0, make_cell(True,  False, False, True ))
    set_cell(maze, 0, 1, make_cell(True,  True,  False, False))
    set_cell(maze, 0, 2, make_cell(True,  False, False, False))
    set_cell(maze, 0, 3, make_cell(True,  False, True,  False))
    set_cell(maze, 0, 4, make_cell(True,  False, False, False))
    set_cell(maze, 0, 5, make_cell(True,  False, False, False))
    set_cell(maze, 0, 6, make_cell(True,  True,  True,  False))

    set_cell(maze, 1, 0, make_cell(False, True,  False, False))
    set_cell(maze, 1, 1, make_cell(False, True,  True,  False))
    set_cell(maze, 1, 2, make_cell(False, False, True,  False))
    set_cell(maze, 1, 3, make_cell(False, True,  True,  False))
    set_cell(maze, 1, 4, make_cell(False, False, True,  False))
    set_cell(maze, 1, 5, make_cell(False, True,  False, False))
    set_cell(maze, 1, 6, make_cell(False, False, True,  False))

    set_cell(maze, 2, 0, make_cell(False, False, False, True ))
    set_cell(maze, 2, 1, make_cell(False, False, False, False))
    set_cell(maze, 2, 2, make_cell(False, False, False, False))
    set_cell(maze, 2, 3, make_cell(False, True,  False, False))
    set_cell(maze, 2, 4, make_cell(False, False, True,  False))
    set_cell(maze, 2, 5, make_cell(False, False, False, False))
    set_cell(maze, 2, 6, make_cell(False, True,  True,  False))

    set_cell(maze, 3, 0, make_cell(False, False, True,  True ))
    set_cell(maze, 3, 1, make_cell(False, False, True,  False))
    set_cell(maze, 3, 2, make_cell(False, True,  False, False))
    set_cell(maze, 3, 3, make_cell(False, False, True,  False))
    set_cell(maze, 3, 4, make_cell(False, False, True,  False))
    set_cell(maze, 3, 5, make_cell(False, True,  False, False))
    set_cell(maze, 3, 6, make_cell(False, False, True,  False))

    set_cell(maze, 4, 0, make_cell(False, False, True,  True ))
    set_cell(maze, 4, 1, make_cell(False, True,  False, False))
    set_cell(maze, 4, 2, make_cell(False, False, True,  False))
    set_cell(maze, 4, 3, make_cell(False, True,  True,  False))
    set_cell(maze, 4, 4, make_cell(False, False, True,  False))
    set_cell(maze, 4, 5, make_cell(False, False, True,  False))
    set_cell(maze, 4, 6, make_cell(False, False, True,  False))

    set_cell(maze, 5, 0, make_cell(False, True,  False, True ))
    set_cell(maze, 5, 1, make_cell(False, True,  True,  False))
    set_cell(maze, 5, 2, make_cell(False, True,  False, False))
    set_cell(maze, 5, 3, make_cell(False, True,  True,  False))
    set_cell(maze, 5, 4, make_cell(False, True,  False, False))
    set_cell(maze, 5, 5, make_cell(False, True,  True,  False))
    set_cell(maze, 5, 6, make_cell(False, True,  False, False))


    ending_row = (MAZE_H - 1) * CELL_SIDE + (CELL_SIDE // 2)
    ending_col = (MAZE_W - 1) * CELL_SIDE + (CELL_SIDE // 2)

    maze[ending_row, ending_col] = MAX_ENERGY
    bfs(maze, ending_row, ending_col, MAX_ENERGY)

    plt.imshow(maze)
    plt.scatter(ending_col, ending_row, color='g', marker='o')
    plt.scatter((CELL_SIDE // 2), CELL_SIDE + (CELL_SIDE // 2), color='r', marker='o')
    gradient_descent(maze, CELL_SIDE // 2, CELL_SIDE + CELL_SIDE // 2)

    plt.show()




if __name__ == '__main__':
    main()