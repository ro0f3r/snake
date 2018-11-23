from movableGameObject import MovableGameObject


class Snake(MovableGameObject):
    def __init__(self, x_range, y_range, thickness, block_size):
        super().__init__(x_range, y_range, thickness, block_size)
        self.direction = "up"

        # snake body
        self.thickness = block_size
        self.length = 1
        self.body_parts = [[self.x_coordinate, self.y_coordinate]]

    # ########  override  ######## #
    def calculate_new_position(self):
        if self.direction == "left":
            self.move_left()
        if self.direction == "right":
            self.move_right()
        if self.direction == "up":
            self.move_up()
        if self.direction == "down":
            self.move_down()


