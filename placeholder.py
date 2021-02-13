from colorama import init, Fore, Back

init(autoreset=True)


class Placeholder:
    def __init__(self):
        self.object = None
        self.has_object = False
        self.has_brick = False
        self.has_power_up = False

    def add_brick(self, obj):
        self.object = obj
        self.has_object = True
        self.has_brick = True

    def add_power_up(self, obj):
        self.object = obj
        self.has_object = True
        self.has_power_up = True

    def remove_object(self):
        self.object = None
        self.has_object = False
        self.has_brick = False
        self.has_power_up = False

    def __str__(self):
        if self.has_object:
            return self.object
        return Back.LIGHTWHITE_EX + "  *  "
