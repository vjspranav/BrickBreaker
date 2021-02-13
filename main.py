from placeholder import Placeholder
from brick import BlueBrick, RedBrick, GreenBrick

grid = []


def initialize(x, y):
    global grid
    for i in range(x):
        for j in range(y):
            grid = [[Placeholder() for j in range(y)] for i in range(x)]


def render():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print("")


if __name__ == '__main__':
    initialize(5, 10)
    grid[1][2] = BlueBrick()
    grid[1][3] = BlueBrick()
    grid[1][4] = RedBrick()
    grid[1][5] = GreenBrick()
    grid[1][6] = BlueBrick()
    grid[1][7] = RedBrick()
    grid[2][3] = RedBrick()
    grid[2][4] = GreenBrick()
    grid[2][5] = BlueBrick()
    grid[2][6] = BlueBrick()
    grid[3][2] = BlueBrick()
    grid[3][3] = BlueBrick()
    grid[3][4] = RedBrick()
    grid[3][5] = GreenBrick()
    grid[3][6] = BlueBrick()
    grid[3][7] = RedBrick()
    render()
