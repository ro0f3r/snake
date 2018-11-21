import random


class Snake:
    def __init__(self, window_width, window_height, block_size):
        # game info
        self.block_size = block_size
        self.window_width = window_width[0]
        self.window_height = [window_height[0], window_height[1]]

        # snake position
        # todo spawn at a proper position mod thickness
        self.x_coordinate = self.window_width // 2
        self.y_coordinate = self.window_height[1] // 2
        self.direction = "up"

        # snake body
        self.thickness = block_size
        self.length = 1
        self.body_parts = [[self.x_coordinate, self.y_coordinate]]

    def __str__(self):
        return "Snake @" + str(self.x_coordinate) + " x " + str(self.y_coordinate)

    def move(self):
        self.calculate_new_position()
        self.check_boundaries()

    def check_boundaries(self):
        # snake goes through right screen border
        if self.x_coordinate >= self.window_width:
            self.x_coordinate = 0
        # snake goes through left screen border
        if self.x_coordinate < 0:
            self.x_coordinate = self.window_width
        # snake goes through bottom border
        if self.y_coordinate >= self.window_height[1]:
            self.y_coordinate = self.window_height[0]
        # snake goes through top border
        if self.y_coordinate < self.window_height[0]:
            self.y_coordinate = self.window_height[1] - self.thickness

    def calculate_new_position(self):
        if self.direction == "left":
            self.move_left()
        if self.direction == "right":
            self.move_right()
        if self.direction == "up":
            self.move_up()
        if self.direction == "down":
            self.move_down()

    def move_left(self):
        self.x_coordinate -= self.block_size

    def move_right(self):
        self.x_coordinate += self.block_size

    def move_up(self):
        self.y_coordinate -= self.block_size

    def move_down(self):
        self.y_coordinate += self.block_size

    def collides_with(self, other):
        if other.get_position()[0] + other.get_thickness() > self.get_position()[0] >= other.get_position()[0] or  \
           other.get_position()[0] < self.get_position()[0] + self.get_thickness() < other.get_position()[0] + other.get_thickness():
            if other.get_position()[1] + other.get_thickness() > self.get_position()[1] > other.get_position()[1]:
                return True
            elif other.get_position()[1] + other.get_thickness() >= self.get_position()[1] + self.get_thickness() > other.get_position()[1]:
                return True
        else:
            return False

    def get_position(self):
        return self.x_coordinate, self.y_coordinate

    def get_thickness(self):
        return self.thickness
