class Placeholder:
    def __init__(self):
        self.object = None
        self.has_object = False

    def add_object(self, obj):
        self.object = obj
        self.has_object = True

    def remove_object(self):
        self.object = None
        self.has_object = False

    def __str__(self):
        if self.has_object:
            return self.object
        return "  *  "
