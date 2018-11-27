from movableGameObject import MovableGameObject


# TODO finish implementing
class SnakeBodyPart(MovableGameObject):
    def __init__(self, x_coordinate, y_coordinate, thickness, direction):
        super().__init__(x_coordinate, y_coordinate, thickness, thickness, inform_about_new_instance=False)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction

    def get_new_x(self):
        return 0

    def get_new_y(self):
        return 0
