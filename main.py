import time
import threading
import sys
from get import getch
from os import system
from geometry import return_closest_point, points_in_line
from placeholder import Placeholder
from paddle import Paddle
from brick import BlueBrick, RedBrick, GreenBrick
from ball import Ball

grid = []
ball = Ball(8, 8)
paddle = [Paddle(0, 14, 10), Paddle(1, 14, 11), Paddle(2, 14, 12)]
curNumPaddles = 3


def has_bricks(points):
    req_points = []
    for point in points:
        if grid[point[0]][point[1]].has_brick:
            req_points.append(point)
    return req_points


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

        # Check ball doesn't cross bounds
        if new_x > len(grid) - 1:
            new_x = len(grid) - 1
        if new_x < 0:
            new_x = 0
        if new_y > len(grid[0]) - 1:
            new_y = len(grid[0]) - 1
        if new_y < 0:
            new_y = 0

        # Handling walls
        if new_x >= len(grid) - 1:
            new_x = len(grid) - 1
            if grid[new_x][new_y].has_paddle or grid[ball.x_pos + 1][ball.y_pos].has_paddle:
                ball.update_velo(-ball.x_vel, ball.y_vel)
                continue
            if ball.lives < 1:
                system("clear")
                print("GAME OVER")
                break
            ball.decrease_life()
            ball.update_position(4, 4)
            ball.update_velo(-1, 1)
            grid[cur_x][cur_y].remove_ball()
            grid[ball.x_pos][ball.y_pos].add_ball(ball)
            time.sleep(0.5)
            continue

        if new_x == 0:
            new_x = 0
            ball.update_velo(-ball.x_vel, ball.y_vel)
            time.sleep(0.5)
            continue
        if new_y >= len(grid[0]) - 1:
            new_y = len(grid[0]) - 1
            ball.update_velo(ball.x_vel, -ball.y_vel)
            time.sleep(0.5)
            continue
        if new_y == 0:
            ball.update_velo(ball.x_vel, -ball.y_vel)
            time.sleep(0.5)
            continue

        # Getting Points that have bricks
        try:
            m = (new_y - cur_y) / (new_x - cur_x)
        except:
            m = 0
        points_with_bricks = points_in_line(cur_x, cur_y, new_x, new_y)
        points_with_bricks = has_bricks(points_with_bricks)
        if len(points_with_bricks) > 1:
            for i in range(len(points_with_bricks) - 1):
                if cur_x == points_with_bricks[i][0] and cur_y == points_with_bricks[i][1]:
                    points_with_bricks.remove(points_with_bricks[i])

        p = 0
        if len(points_with_bricks) > 0:
            p = points_with_bricks[0]

        if len(points_with_bricks) > 1:
            p = return_closest_point(cur_x, cur_y, points_with_bricks)

        # Handling brick collision
        if p:
            vel_x = ball.x_vel
            vel_y = ball.y_vel
            brick_x = p[0]
            brick_y = p[1]
            if vel_y > 0 and vel_x > 0:
                if m == 1:
                    new_x = brick_x - 1
                    new_y = brick_y - 1
                    # Checking if vertical or horizontal blocks exist
                    if grid[brick_x][brick_y - 1].has_brick:
                        brick_y = brick_y - 1
                        ball.update_velo(-ball.x_vel, ball.y_vel)
                    elif grid[brick_x - 1][brick_y].has_brick:
                        brick_x = brick_x - 1
                        ball.update_velo(ball.x_vel, -ball.y_vel)
                    else:
                        ball.update_velo(-ball.x_vel, -ball.y_vel)
                if m < 1:
                    new_x = brick_x
                    new_y = brick_y - 1
                    ball.update_velo(ball.x_vel, -ball.y_vel)
                if m > 1:
                    new_x = brick_x - 1
                    new_y = brick_y
                    ball.update_velo(-ball.x_vel, ball.y_vel)
            elif vel_y > 0 and vel_x < 0:
                if m == -1:
                    new_x = brick_x + 1
                    new_y = brick_y - 1
                    if grid[brick_x][brick_y - 1].has_brick:
                        brick_y = brick_y - 1
                        ball.update_velo(-ball.x_vel, ball.y_vel)
                    elif grid[brick_x + 1][brick_y].has_brick:
                        brick_x = brick_x + 1
                        ball.update_velo(ball.x_vel, -ball.y_vel)
                    else:
                        ball.update_velo(-ball.x_vel, -ball.y_vel)
                if m < -1:
                    new_x = brick_y - 1
                    new_y = brick_x
                    ball.update_velo(ball.x_vel, -ball.y_vel)
                if m > -1:
                    new_x = brick_x + 1
                    new_y = brick_y
                    ball.update_velo(-ball.x_vel, ball.y_vel)

            elif vel_y < 0 and vel_x > 0:
                if m == -1:
                    new_x = brick_x - 1
                    new_y = brick_y + 1
                    if grid[brick_x][brick_y + 1].has_brick:
                        brick_y = brick_y + 1
                        ball.update_velo(-ball.x_vel, ball.y_vel)
                    elif grid[brick_x - 1][brick_y].has_brick:
                        brick_x = brick_x - 1
                        ball.update_velo(ball.x_vel, -ball.y_vel)
                    else:
                        ball.update_velo(-ball.x_vel, -ball.y_vel)
                if m > -1:
                    new_x = brick_x
                    new_y = brick_y + 1
                    ball.update_velo(ball.x_vel, -ball.y_vel)

                if m < -1:
                    new_x = brick_x - 1
                    new_y = brick_y
                    ball.update_velo(-ball.x_vel, ball.y_vel)

            elif vel_y < 0 and vel_x < 0:
                if m == 1:
                    new_x = brick_x + 1
                    new_y = brick_y + 1
                    if grid[brick_x][brick_y + 1].has_brick:
                        brick_y = brick_y + 1
                        ball.update_velo(-ball.x_vel, ball.y_vel)
                    elif grid[brick_x + 1][brick_y]:
                        brick_x = brick_x + 1
                        ball.update_velo(ball.x_vel, -ball.y_vel)
                    else:
                        ball.update_velo(-ball.x_vel, -ball.y_vel)
                if m > 1:
                    new_x = brick_x
                    new_y = brick_y + 1
                    ball.update_velo(ball.x_vel, -ball.y_vel)

                if m < 1:
                    new_x = brick_x + 1
                    new_y = brick_y
                    ball.update_velo(-ball.x_vel, ball.y_vel)

            ball.update_position(new_x, new_y)
            grid[cur_x][cur_y].remove_ball()
            grid[ball.x_pos][ball.y_pos].add_ball(ball)
            grid[brick_x][brick_y].collide()

        ball.update_position(new_x, new_y)
        grid[cur_x][cur_y].remove_ball()
        grid[ball.x_pos][ball.y_pos].add_ball(ball)
        system("clear")
        render()
        time.sleep(0.5)


def inp():
    while True:
        dir = getch()
        # dir = sys.stdin.read(1)
        if dir == "a" or dir == "A":
            if (paddle[0].y > 0):
                for i in range(len(paddle)):
                    grid[paddle[i].x][paddle[i].y].remove_paddle()
                    paddle[i].update_y(paddle[i].y - 1)
        if dir == "d" or dir == "D":
            if paddle[len(paddle) - 1].y < len(grid[0]) - 1:
                for i in range(len(paddle)):
                    grid[paddle[i].x][paddle[i].y].remove_paddle()
                    paddle[i].update_y(paddle[i].y + 1)
        for i in range(len(paddle)):
            grid[paddle[i].x][paddle[i].y].add_paddle(paddle[i])


if __name__ == '__main__':
    initialize(15, 17)
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
    grid[paddle[0].x][paddle[0].y].add_paddle(paddle[0])
    grid[paddle[1].x][paddle[1].y].add_paddle(paddle[1])
    grid[paddle[2].x][paddle[2].y].add_paddle(paddle[2])
    ball.update_velo(-1, -1)
    t1 = threading.Thread(target=inp)
    t1.start()
    move()
    t1.join()
