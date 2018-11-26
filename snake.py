from movableGameObject import MovableGameObject
from snakeBodyPart import SnakeBodyPart


class Snake(MovableGameObject):
    def __init__(self, x_range, y_range, thickness, block_size):
        super().__init__(x_range, y_range, thickness, block_size)

        # snake body
        self.thickness = block_size
        self.length = 1
        self.body_parts = [SnakeBodyPart(self.x_coordinate, self.y_coordinate, self.thickness)]

    def __len__(self):
        return self.length

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

        self.calculate_body()

    def calculate_body(self):
        self.body_parts.append(SnakeBodyPart(self.x_coordinate, self.y_coordinate, self.thickness))

        if len(self.body_parts) > len(self):
            del self.body_parts[0]

        # for segment in snake_list[:-1]:
        #     if segment == snake_head:
        #         game_over = True
        #


