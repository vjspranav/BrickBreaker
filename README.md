## BrickBreaker Game
The code is a simple implementation of BrickBreaker Game in pure terminal without using any curses or GUI Libraries

## Pre-Requisites (Linux)
* Make sure you have venv installed
```
sudo apt-get install python3-venv
```
> Other distros Pretty sure you can figure it out

* Create a new venv
```
python3 -m venv ./venv/
```

## To Install
To install all the requirements
```
make install
```

## To run
```
make run
```

## Game instructions
* Use **a** and **d** to move paddle left and right
* Space to launch the ball
* Use **n** to advance to next level


## Other instructions
* There is one power up that extends the size of paddle
* A user has 3 + 1 (4) Lives
* If ball hits bottom wall, life is lost
* If paddle takes bomb from boss monster life is lost.
* To kill boss monster it needs to be hit 10 times