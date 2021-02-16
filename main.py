import time
from os import system
from placeholder import Placeholder
from brick import BlueBrick, RedBrick, GreenBrick
from ball import Ball

grid = []
ball = Ball(5, 5)

def initialize(x, y):
    global grid
    for i in range(x):
        for j in range(y):
            grid = [[Placeholder() for j in range(y)] for i in range(x)]


def render():
    print("Num Lives : ", ball.lives)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print("")
    print("Ball Cur X Pos: ", ball.x_pos, "\nCur Y Pos: ", ball.y_pos)
    print("Ball Cur X Vel: ", ball.x_vel, "\nCur Y Vel: ", ball.y_vel)

def move():
    while True:
        cur_x, cur_y = ball.x_pos, ball.y_pos
        new_x, new_y = ball.x_pos + ball.x_vel, ball.y_pos + ball.y_vel

        # Handling walls
        if new_x >= len(grid)-1:
            if ball.lives < 1 :
                system("clear")
                print("GAME OVER")
                break
            ball.decrease_life()
            ball.update_position(4, 4)
            ball.update_velo(-1, 1)
            grid[cur_x][cur_y].remove_ball()
            grid[ball.x_pos][ball.y_pos].add_ball(ball)
            continue

        if new_x == 0:
            new_x = 0
            ball.update_velo(-ball.x_vel, ball.y_vel)
        if new_y >= len(grid[0])-1:
            new_y = len(grid[0])-1
            ball.update_velo(ball.x_vel, -ball.y_vel)
        if new_y == 0:
            new_y = 0
            ball.update_velo(ball.x_vel, -ball.y_vel)

        # Handling bricks
        if grid[new_x][new_y].has_brick:
            grid[new_x][new_y].collide()
            new_y = cur_y
            if abs(new_x - cur_x) == 1:
                ball.update_velo(-ball.x_vel, ball.y_vel)
            ball.update_position(new_x, new_y)
            grid[cur_x][cur_y].remove_ball()
            grid[new_x][new_y].add_ball(ball)
            continue

        if grid[cur_x][new_y].has_brick:
            grid[cur_x][new_y].collide()
            new_x=cur_x
            ball.update_velo(ball.x_vel, -ball.y_vel)
            ball.update_position(new_x, new_y)
            grid[cur_x][cur_y].remove_ball()
            grid[new_x][new_y].add_ball(ball)
            continue

        ball.update_position(new_x, new_y)
        grid[cur_x][cur_y].remove_ball()
        grid[ball.x_pos][ball.y_pos].add_ball(ball)
        system("clear")
        render()
        time.sleep(0.5)


if __name__ == '__main__':
    initialize(15, 20)
    grid[1][2].add_brick(BlueBrick())
    grid[1][3].add_brick(BlueBrick())
    grid[1][4].add_brick(RedBrick())
    grid[1][5].add_brick(GreenBrick())
    grid[1][6].add_brick(BlueBrick())
    grid[1][7].add_brick(RedBrick())
    grid[2][3].add_brick(RedBrick())
    grid[2][4].add_brick(GreenBrick())
    grid[2][5].add_brick(BlueBrick())
    grid[2][6].add_brick(BlueBrick())
    grid[3][2].add_brick(BlueBrick())
    grid[3][3].add_brick(BlueBrick())
    grid[3][4].add_brick(RedBrick())
    grid[3][5].add_brick(GreenBrick())
    grid[3][6].add_brick(BlueBrick())
    grid[7][1].add_brick(GreenBrick())
    grid[ball.x_pos][ball.y_pos].add_ball(ball)
    ball.update_velo(-1, 3)
    move()