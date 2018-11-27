from movableGameObject import MovableGameObject
from snakeBodyPart import SnakeBodyPart


class Snake(MovableGameObject):
    def __init__(self, x_range, y_range, thickness, block_size):
        super().__init__(x_range, y_range, thickness, block_size)

        # snake body
        self.thickness = block_size
        self.length = 0
        self.head = SnakeBodyPart(self.x_coordinate, self.y_coordinate, self.thickness, self.direction)
        self.body_parts = []

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
        self.body_parts.append(self.head)

        self.head = SnakeBodyPart(self.x_coordinate, self.y_coordinate, self.thickness, self.direction)

        new_body_parts = []

        for i in range(len(self.body_parts)):
            try:
                if self.body_parts[i].get_direction() == "right" and self.body_parts[i + 1].get_direction() == "down":
                    new_body_parts.append(SnakeBodyPart(self.body_parts[i + 1].get_x_position(), self.body_parts[i + 1].get_y_position(), self.get_thickness(), "right-down"))
                    print("YES")
                else:
                    new_body_parts.append(SnakeBodyPart(self.body_parts[i + 1].get_x_position(), self.body_parts[i + 1].get_y_position(), self.get_thickness(), self.body_parts[i + 1].get_direction()))

            except IndexError:
                new_body_parts.append(SnakeBodyPart(self.head.get_x_position(), self.head.get_y_position(), self.get_thickness(), self.head.get_direction()))

        if len(self.body_parts) > len(self):
            del self.body_parts[0]

    def get_head(self):
        return self.head

    def get_body_parts(self):
        return self.body_parts

        # for segment in snake_list[:-1]:
        #     if segment == snake_head:
        #         game_over = True
        #


