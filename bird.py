from movableGameObject import MovableGameObject


class Bird(MovableGameObject):
    def __init__(self, x_position, y_position, direction, thickness, block_size, playfield_height_range):
        super().__init__(x_position, y_position, thickness, block_size)
        self.x_coordinate = x_position
        self.y_coordinate = y_position
        self.playfield_height_range = playfield_height_range
        self.direction = direction

    def calculate_new_position(self):
        if self.direction == "up":
            if self.y_coordinate > self.playfield_height_range[0]:
                self.move_up()
            elif self.y_coordinate <= self.playfield_height_range[0]:
                self.direction = "down"
                self.move_down()
        elif self.direction == "down":
            if self.y_coordinate < self.playfield_height_range[1]:
                self.move_down()
            elif self.y_coordinate >= self.playfield_height_range[1]:
                self.direction = "up"
                self.move_up()

    def get_new_x(self):
        pass

    def get_new_y(self):
        pass

