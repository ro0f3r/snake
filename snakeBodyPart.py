from gameObject import GameObject


# TODO finish implementing
class SnakeBodyPart(GameObject):
    def __init__(self, x_coordinate, y_coordinate, thickness):
        super().__init__(x_coordinate, y_coordinate, thickness, inform_about_new_instance=False)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_new_x(self):
        return 0

    def get_new_y(self):
        return 0
