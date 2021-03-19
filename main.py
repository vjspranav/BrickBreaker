import time
import threading
from get import getch
from os import system
from geometry import return_closest_point, points_in_line
from placeholder import Placeholder
from paddle import Paddle
from brick import BlueBrick, RedBrick, GreenBrick, InvicibleBrick, BombBrick, RainbowBrick, BossBrick
from power_up import Expand, Bomb
from ball import Ball

grid = []
paddle = [Paddle(0, 14, 10), Paddle(1, 14, 11), Paddle(2, 14, 12)]
power_ups = []
ball = Ball(13, 11)
curNumPaddles, score = 3, 0
is_attached = True
sleep = 100
num_levels = 4

# debug
num_hit = 1

level = 0


def inp_check():
    while True and num_bricks > 0 and level <= num_levels:
        old_number = num_hit
        time.sleep(0.5)
        if old_number == num_hit:
            t1 = threading.Thread(target=inp)
            t1.start()
    exit()
    return


# Functions run in threads
# Input for paddle control
def inp():
    global num_bricks
    global is_attached
    global num_hit
    while True and num_bricks > 0:
        # Catch what you can't fix
        try:
            dir_input = getch()
            if dir_input == "a" or dir_input == "A":
                if paddle[0].y > 0:
                    if level == num_levels:
                        grid[0][paddle[1].y-1].add_brick(grid[0][paddle[1].y].get_object())
                        grid[0][paddle[1].y].remove_object()
                    for i in range(len(paddle)):
                        grid[paddle[i].x][paddle[i].y].remove_paddle()
                        paddle[i].update_y(paddle[i].y - 1)
            elif dir_input == "d" or dir_input == "D":
                if paddle[len(paddle) - 1].y < len(grid[0]) - 1:
                    if level == num_levels:
                        grid[0][paddle[1].y + 1].add_brick(grid[0][paddle[1].y].get_object())
                        grid[0][paddle[1].y].remove_object()
                    for i in range(len(paddle)):
                        grid[paddle[i].x][paddle[i].y].remove_paddle()
                        paddle[i].update_y(paddle[i].y + 1)
            elif dir_input == "n" or dir_input == "N":
                next_level()
                if level > num_levels:
                    exit()
                    return
                system("clear")
                render()

            elif dir_input == " ":
                if is_attached:
                    ball.update_velo(-1, -1)
                    is_attached = False
                    continue

            if is_attached:
                grid[ball.x_pos][ball.y_pos].remove_ball()
                ball.update_position(ball.x_pos, paddle[round(len(paddle) / 2) - 1].y)
                grid[ball.x_pos][ball.y_pos].add_ball(ball)

            for i in range(len(paddle)):
                grid[paddle[i].x][paddle[i].y].add_paddle(paddle[i])
            num_hit += 1
        except Exception:
            pass
        finally:
            continue


# Activates power up on collision with paddle
def activate_power_up(power_up):
    global curNumPaddles
    timer = 0
    # Expand
    if power_up.number == 0:
        if len(paddle) <= 3:
            p4 = Paddle(4, 14, len(paddle))
            p5 = Paddle(5, 14, len(paddle) + 1)
            paddle.append(p4)
            paddle.append(p5)
            grid[14][p4.y].add_paddle(p4)
            grid[14][p5.y].add_paddle(p5)
            while timer < 15:
                time.sleep(1)
                timer += 1
            grid[14][p4.y].remove_paddle()
            grid[14][p5.y].remove_paddle()
            paddle.remove(p4)
            paddle.remove(p5)
            power_ups.remove(power_up)
            return 1
    if power_up.number == 1:
        ball.decrease_life()
        power_ups.remove(power_up)


# On brick destroy makes power up move downward
def move_power_up(power_up):
    while True:
        time.sleep(0.5)
        grid[power_up.x_pos][power_up.y_pos].remove_power_up()
        new_x = power_up.x_pos
        new_y = power_up.y_pos
        if level != 4:
            new_x = power_up.x_pos + power_up.x_vel
            new_y = power_up.y_pos + power_up.y_vel
            if new_x <= 0 or new_x >= len(grid):
                new_x = power_up.x_pos
                power_up.update_velocity(0, power_up.y_vel)
            if new_y <= 0 or new_y >= len(grid[0]):
                new_y = power_up.y_pos
                power_up.update_velocity(power_up.x_vel, 0)
        else:
            new_x = new_x + 1
        power_up.update_position(new_x, new_y)
        if power_up.x_pos >= len(grid):
            break
        if grid[power_up.x_pos][power_up.y_pos].has_paddle:
            power_ups.append(power_up)
            system('aplay -q ./sounds/power_up.wav&')
            p = threading.Thread(target=activate_power_up, args=(power_up,))
            p.start()
            p.join()
            break
        grid[power_up.x_pos][power_up.y_pos].add_power_up(power_up)


# Driver Functions

def clear_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j].clear()


# Creates Brick Pattern
def add_bricks():
    if level == 1:
        grid[1][2].add_brick(BlueBrick())
        grid[1][3].add_brick(BlueBrick())
        grid[1][4].add_brick(RedBrick())
        grid[1][5].add_brick(GreenBrick())
        grid[1][6].add_brick(BlueBrick())
        grid[1][7].add_brick(RedBrick())
        grid[1][8].add_brick(RedBrick())
        grid[1][9].add_brick(GreenBrick())
        grid[1][10].add_brick(BlueBrick())
        grid[1][11].add_brick(BlueBrick())
        grid[1][12].add_brick(InvicibleBrick())
        grid[2][3].add_brick(RedBrick())
        grid[2][4].add_brick(GreenBrick())
        grid[2][5].add_brick(BlueBrick())
        grid[2][6].add_brick(BombBrick())
        grid[2][7].add_brick(BombBrick())
        grid[2][8].add_brick(BombBrick())
        grid[2][9].add_brick(BombBrick())
        grid[2][10].add_brick(BombBrick())
        grid[2][11].add_brick(BombBrick())
        grid[3][2].add_brick(BlueBrick())
        grid[3][3].add_brick(BlueBrick())
        grid[3][4].add_brick(RedBrick())
        grid[3][5].add_brick(GreenBrick())
        grid[3][6].add_brick(InvicibleBrick())
        grid[3][7].add_brick(BlueBrick())
        grid[3][8].add_brick(GreenBrick())
        grid[3][9].add_brick(RedBrick())
        grid[3][10].add_brick(GreenBrick())
        grid[3][11].add_brick(InvicibleBrick())
        grid[3][12].add_brick(GreenBrick())
        grid[4][3].add_brick(BombBrick())
        grid[4][4].add_brick(BombBrick())
        grid[4][5].add_brick(BombBrick())
        grid[4][6].add_brick(BombBrick())
        grid[4][7].add_brick(BombBrick())
        grid[4][8].add_brick(BombBrick())
        grid[4][9].add_brick(RedBrick())
        grid[4][10].add_brick(BlueBrick())
        grid[4][11].add_brick(BlueBrick())
        grid[5][2].add_brick(GreenBrick())
        grid[5][3].add_brick(BlueBrick())
        grid[5][4].add_brick(GreenBrick())
        grid[5][5].add_brick(BlueBrick())
        grid[5][6].add_brick(GreenBrick())
        grid[5][7].add_brick(BlueBrick())
        grid[5][8].add_brick(GreenBrick())
        grid[5][9].add_brick(BlueBrick())
        grid[5][10].add_brick(GreenBrick())
        grid[5][11].add_brick(BlueBrick())
        grid[5][12].add_brick(GreenBrick())
        #Power Ups
        expand = Expand(2, 5)
        grid[expand.x_pos][expand.y_pos].add_power_up(expand)
    elif level == 2:
        grid[5][2].add_brick(GreenBrick())
        grid[5][3].add_brick(BlueBrick())
        grid[5][4].add_brick(RainbowBrick())
        grid[5][5].add_brick(BlueBrick())
        grid[5][6].add_brick(GreenBrick())
        grid[5][7].add_brick(BlueBrick())
        grid[5][8].add_brick(RainbowBrick())
        grid[5][9].add_brick(BlueBrick())
    elif level == 3:
        grid[3][2].add_brick(BlueBrick())
        grid[3][3].add_brick(BlueBrick())
        grid[3][4].add_brick(RedBrick())
        grid[3][5].add_brick(GreenBrick())
        grid[3][6].add_brick(InvicibleBrick())
        grid[3][7].add_brick(BlueBrick())
        grid[3][8].add_brick(GreenBrick())
        grid[3][9].add_brick(RedBrick())
    elif level == 4:
        grid[0][paddle[1].y].add_brick(BossBrick())


# For Boss
def add_boss_bricks(num):
    if num == 1:
        grid[3][0].add_brick(BlueBrick())
        grid[3][1].add_brick(BlueBrick())
        grid[3][2].add_brick(BlueBrick())
        grid[3][3].add_brick(BlueBrick())
        grid[3][4].add_brick(RedBrick())
        grid[3][5].add_brick(GreenBrick())
        grid[3][6].add_brick(InvicibleBrick())
        grid[3][7].add_brick(BlueBrick())
        grid[3][8].add_brick(GreenBrick())
        grid[3][9].add_brick(RedBrick())
        grid[3][10].add_brick(RedBrick())
        grid[3][11].add_brick(RedBrick())
        grid[3][12].add_brick(RedBrick())
        grid[3][13].add_brick(RedBrick())

    if num == 2:
        grid[3][0].add_brick(BlueBrick())
        grid[3][1].add_brick(BlueBrick())
        grid[3][2].add_brick(BlueBrick())
        grid[3][3].add_brick(BlueBrick())
        grid[3][4].add_brick(RedBrick())
        grid[3][5].add_brick(GreenBrick())
        grid[3][6].add_brick(InvicibleBrick())
        grid[3][7].add_brick(BlueBrick())
        grid[3][8].add_brick(GreenBrick())
        grid[3][9].add_brick(RedBrick())
        grid[3][10].add_brick(RedBrick())
        grid[3][11].add_brick(RedBrick())
        grid[3][12].add_brick(RedBrick())
        grid[3][13].add_brick(RedBrick())


def next_level():
    clear_grid()
    global is_attached, level, num_bricks
    if level > num_levels:
        system("clear")
        print("Thank You For playing")
        global num_bricks
        num_bricks = 0
        exit()
    system('aplay -q ./sounds/level.wav&')
    level += 1
    is_attached = True
    grid[ball.x_pos][ball.y_pos].remove_ball()
    ball.update_position(13, 11)
    ball.update_velo(0, 0)
    grid[ball.x_pos][ball.y_pos].add_ball(ball)
    grid[paddle[0].x][paddle[0].y].add_paddle(paddle[0])
    grid[paddle[1].x][paddle[1].y].add_paddle(paddle[1])
    grid[paddle[2].x][paddle[2].y].add_paddle(paddle[2])
    add_bricks()


# Gets Points having bricks from a list of points
def has_bricks(points):
    req_points = []
    for point in points:
        if grid[point[0]][point[1]].has_brick:
            req_points.append(point)
    return req_points


# If brick add score and destroy brick (Irrespective of type)
def destroy(x, y):
    global score
    if grid[x][y].has_brick:
        if grid[x][y].get_object().num_lives > 0:
            score += grid[x][y].get_object().num_lives
        elif grid[x][y].get_object().num_lives == -2:
            score += 1
            bombard(x, y)
        elif grid[x][y].get_object().num_lives == -1:
            score += 1
        grid[x][y].remove_object()
        if grid[x][y].has_power_up:
            grid[x][y].get_power_up().update_velocity(ball.x_vel, -ball.y_vel)
            p = threading.Thread(target=move_power_up, args=(grid[x][y].get_power_up(),))
            p.start()
        system("clear")
        render()
        time.sleep(0.1)


# Special brick call destroy on all adjacent bricks
def bombard(x, y):
    system('aplay -q ./sounds/blast.wav&')
    grid[x][y].remove_object()
    destroy(x, y - 1)
    destroy(x - 1, y - 1)
    destroy(x - 1, y)
    destroy(x - 1, y + 1)
    destroy(x, y + 1)
    destroy(x + 1, y + 1)
    destroy(x + 1, y)
    destroy(x + 1, y - 1)


# Initializing the grid
def initialize(x, y):
    global grid
    for i in range(x):
        for j in range(y):
            grid = [[Placeholder() for _ in range(y)] for _ in range(x)]


num_bricks = 1


# Renders View
def render():
    # Legend
    print(RedBrick(), " - 3 Points ", BlueBrick(), " - 2 Points ", GreenBrick(), " - 1 Point\n" + str(InvicibleBrick()),
          " - Cannot be broken ", BombBrick(), " - Destroy all bricks around\n")
    global num_bricks
    num_bricks = 0
    print("Num Lives : ", ball.lives, "\tCur Score : ", score, "\tTime before moving down: ", abs(round(sleep / 10, 0)), "\tLevel: ", level)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
            if grid[i][j].has_brick:
                grid[i][j].get_object().change_color()
                if grid[i][j].get_object().num_lives > 0:
                    num_bricks += 1

        print("")
    if level < 3 and num_bricks == 0:
         num_bricks=1
         next_level()

    if level == 4:
        if grid[0][paddle[1].y].has_brick:
            print("Boss Health: [", end="")
            for _ in range(grid[0][paddle[1].y].get_object().num_lives):
                print("=", end="")
            for _ in range(10 - grid[0][paddle[1].y].get_object().num_lives):
                print(" ", end="")
            print("]")
    else:
        print("\n", Expand(-1, -1), " - Expand size of paddle by 2 (max till length 5) for 15 seconds")


def move_bricks_down():
    global num_bricks
    if level == 4:
        return
    for i in range(len(grid) - 2, -1, -1):
        for j in range(len(grid[0])):
            if grid[i][j].has_brick:
                grid[i + 1][j].add_brick(grid[i][j].get_object())
                grid[i][j].remove_object()
                if grid[i][j].has_power_up:
                    grid[i + 1][j].add_power_up(grid[i][j].get_power_up())
                    grid[i][j].remove_power_up()
                    grid[i + 1][j].get_power_up().update_position(i+1, j)

    for i in range(len(grid[0])):
        if grid[len(grid) - 1][i].has_brick:
            system("clear")
            print("GAME OVER")
            num_bricks = 0
            return -1


# Moves ball (Also causes continuous render)
def move():
    global score
    global sleep
    num = 100
    while True and level <= num_levels:
        if is_attached:
            system("clear")
            render()
            time.sleep(0.5)
            continue

        if level > num_levels:
            return

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
            try:
                if grid[new_x][new_y].has_paddle or grid[ball.x_pos + 1][ball.y_pos].has_paddle:
                    if not grid[new_x][new_y].has_paddle:
                        new_x = ball.x_pos + 1
                        new_y = ball.y_pos
                    p_no = grid[new_x][new_y].get_paddle().number

                    # Variable velocity and deflection works!!
                    if p_no < round(len(paddle) / 2) - 1:
                        if ball.y_vel > 0:
                            new_vel_x = -ball.x_vel
                            new_vel_y = -ball.y_vel  # +1
                        else:
                            new_vel_x = -ball.x_vel
                            new_vel_y = ball.y_vel  # -1
                    elif p_no == round(len(paddle) / 2) - 1:
                        new_vel_x = -ball.x_vel
                        new_vel_y = -ball.y_vel
                    else:
                        if ball.y_vel < 0:
                            new_vel_x = -ball.x_vel
                            new_vel_y = -ball.y_vel  # - 1
                        else:
                            new_vel_x = -ball.x_vel
                            new_vel_y = ball.y_vel  # + 1
                    if sleep < 0:
                        if level == 4:
                            bomb = Bomb(1, paddle[1].y)
                            grid[bomb.x_pos][bomb.y_pos].add_power_up(bomb)
                            p = threading.Thread(target=move_power_up, args=(bomb,))
                            p.start()
                            sleep = 100
                        elif move_bricks_down() == -1:
                            return -1
                    system('aplay -q ./sounds/bounce.wav&')
                    if new_vel_x > 3:
                        new_vel_x = 3
                    if new_vel_y > 3:
                        new_vel_y = 3
                    if new_vel_x < -3:
                        new_vel_x = -3
                    if new_vel_y < -3:
                        new_vel_y = -3
                    ball.update_velo(new_vel_x, new_vel_y)
                    continue
            except IndexError:
                return

            if ball.lives < 1:
                system("clear")
                print("GAME OVER")
                return -1
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
        if new_y >= len(grid[0]) - 1:
            new_y = len(grid[0]) - 1
            ball.update_velo(ball.x_vel, -ball.y_vel)
        if new_y == 0:
            ball.update_velo(ball.x_vel, -ball.y_vel)

        # Getting Points that have bricks
        try:
            m = (new_y - cur_y) / (new_x - cur_x)
        except ZeroDivisionError:
            m = 0
        points_with_bricks = points_in_line(cur_x, cur_y, new_x, new_y)
        points_with_bricks = has_bricks(points_with_bricks)
        if len(points_with_bricks) > 1:
            for i in range(len(points_with_bricks) - 1):
                if cur_x == points_with_bricks[i][0] and cur_y == points_with_bricks[i][1]:
                    points_with_bricks.remove(points_with_bricks[i])

        p = []
        if len(points_with_bricks) == 1:
            p = points_with_bricks[0]

        if len(points_with_bricks) > 1:
            p = return_closest_point(cur_x, cur_y, points_with_bricks)

        # Handling brick collision
        if len(p) > 0:
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
            elif vel_y > 0 > vel_x:
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

            elif vel_y < 0 < vel_x:
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
                    elif grid[brick_x + 1][brick_y].has_brick:
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
            if grid[brick_x][brick_y].get_object().num_lives == -2:
                bombard(brick_x, brick_y)
            cur_point = grid[brick_x][brick_y].collide()
            system('aplay -q ./sounds/collision.wav&')
            # For Boss level
            if level == 4:
                if grid[0][paddle[1].y].has_brick:
                    if grid[0][paddle[1].y].get_object().num_lives == 5:
                        add_boss_bricks(1)
                    if grid[0][paddle[1].y].get_object().num_lives == 2:
                        add_boss_bricks(2)
                if grid[0][paddle[1].y].get_object().num_lives <= 0:
                    system("clear")
                    print("game over")
                    exit()
                    return
            score += cur_point
            if not grid[brick_x][brick_y].has_brick:
                if grid[brick_x][brick_y].has_power_up:
                    threading.Thread(target=move_power_up, args=(grid[brick_x][brick_y].get_power_up(),)).start()

        ball.update_position(new_x, new_y)
        grid[cur_x][cur_y].remove_ball()
        grid[ball.x_pos][ball.y_pos].add_ball(ball)
        system("clear")
        render()
        print("Active Power Ups: ", power_ups)
        if num_bricks <= 0 and level > 3:
            break
        time.sleep(0.5)
        if sleep > 0:
            sleep -= 3
            continue


if __name__ == '__main__':
    # Grid
    initialize(15, 17)
    # Adding Bricks
    next_level()
    t1 = threading.Thread(target=inp)
    t1.start()
    t2 = threading.Thread(target=inp_check)
    t2.start()
    # p1 = threading.Thread(target=move_power_up, args=(expand,))
    # p1.start()
    move()
    #t1.join()
    # p1.join()
    system("clear")
    print("Thank you for playing")
