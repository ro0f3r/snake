import random


class GameObject:
    def __init__(self, x_range, y_range, thickness):
        self.thickness = thickness
        self.x_range = x_range
        self.y_range = y_range
        self.x_coordinate = self.get_new_x()
        self.y_coordinate = self.get_new_y()
        print("new " + str(self))

    def __str__(self):
        return type(self).__name__ + " @" + str(self.x_coordinate) + " x " + str(self.y_coordinate)

    def get_new_x(self):
        return GameObject.get_new_position_from_range(self.x_range, self.thickness)

    def get_new_y(self):
        return GameObject.get_new_position_from_range(self.y_range, self.thickness)

    @staticmethod
    def get_new_position_from_range(axis_range, thickness):
        return random.randrange(axis_range[0], axis_range[1] - thickness) // thickness * thickness

    def get_thickness(self):
        return self.thickness

    def get_x_position(self):
        return self.x_coordinate

    def get_y_position(self):
        return self.y_coordinate

    def get_position(self):
        return [self.get_x_position(), self.get_y_position()]

    def get_position_thickness_thickness(self):
        return [self.x_coordinate, self.y_coordinate, self.thickness, self.thickness]
