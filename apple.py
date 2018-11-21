import random


class Apple:
    def __init__(self, x_range, y_range):
        self.thickness = 20
        self.x_coordinate = self.get_x(x_range)
        self.y_coordinate = self.get_y(y_range)
        self.is_eaten = False

    def get_x(self, x_range):
        return round(random.randrange(x_range[0], x_range[1] - self.thickness) / self.thickness) * self.thickness

    def get_y(self, y_range):
        return round(random.randrange(y_range[0], y_range[1] - self.thickness) / self.thickness) * self.thickness

    def __str__(self):
        return "Apple @" + str(self.x_coordinate) + " x " + str(self.y_coordinate)

    def get_position(self):
        return [self.x_coordinate, self.y_coordinate, self.thickness, self.thickness]

    def get_thickness(self):
        return self.thickness
