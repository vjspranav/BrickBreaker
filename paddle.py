class Paddle:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_y(self, y):
        self.y = y

    def __str__(self):
        return "====="
