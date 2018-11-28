from movableGameObject import MovableGameObject
from snakeBodyPart import SnakeBodyPart


class Snake(MovableGameObject):
    def __init__(self, x_range, y_range, thickness, block_size):
        super().__init__(x_range, y_range, thickness, block_size)

        # snake body
        self.thickness = block_size
        self.length = 1
        self.head = SnakeBodyPart(self.x_coordinate, self.y_coordinate, self.thickness, self.direction)
        self.body_parts = []

    def __len__(self):
        return self.length

    # ########  override  ######## #
    def calculate_new_position(self):
        if self.head.direction == "left":
            self.move_left()
        if self.head.direction == "right":
            self.move_right()
        if self.head.direction == "up":
            self.move_up()
        if self.head.direction == "down":
            self.move_down()

        self.calculate_body()

    def calculate_body(self):
        self.body_parts.append(self.head)

        self.head = SnakeBodyPart(self.x_coordinate, self.y_coordinate, self.thickness, self.head.direction)

        if len(self.body_parts) > len(self):
            del self.body_parts[0]

        for part in self.body_parts:
            print(part.get_direction())

    def get_head(self):
        return self.head

    def get_body_parts(self):
        return self.body_parts

        # for segment in snake_list[:-1]:
        #     if segment == snake_head:
        #         game_over = True
        #


