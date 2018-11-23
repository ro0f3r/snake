from gameObject import GameObject


class MovableGameObject(GameObject):
    def __init__(self, x_range, y_range, thickness, block_size):
        self.block_size = block_size
        self.window_width = x_range
        self.window_height = y_range
        super().__init__(x_range, y_range, thickness)

    # ########  override  ######## #
    def get_new_x(self):
        return self.get_middle_of_range_by_block_size(self.x_range, self.block_size)

    # ########  override  ######## #
    def get_new_y(self):
        return self.get_middle_of_range_by_block_size(self.y_range, self.block_size)

    @staticmethod
    def get_middle_of_range_by_block_size(axis_range, block_size):
        if isinstance(axis_range, int):
            return axis_range // (2 * block_size) * block_size
        # TODO implement middle of range
        elif len(axis_range) == 2:
            return (axis_range[0] + axis_range[1]) // (2 * block_size) * block_size
        else:
            return 0

    def move(self):
        self.calculate_new_position()
        self.check_boundaries()

    def calculate_new_position(self):
        pass

    def move_left(self):
        self.x_coordinate -= self.block_size

    def move_right(self):
        self.x_coordinate += self.block_size

    def move_up(self):
        self.y_coordinate -= self.block_size

    def move_down(self):
        self.y_coordinate += self.block_size

    def check_boundaries(self):
        # snake goes through right screen border
        if self.x_coordinate >= self.window_width[1]:
            self.x_coordinate = self.window_width[0]
        # snake goes through left screen border
        if self.x_coordinate < self.window_width[0]:
            self.x_coordinate = self.window_width[1]
        # snake goes through bottom border
        if self.y_coordinate >= self.window_height[1]:
            self.y_coordinate = self.window_height[0]
        # snake goes through top border
        if self.y_coordinate < self.window_height[0]:
            self.y_coordinate = self.window_height[1] - self.thickness

    def collides_with(self, other):
        if other.get_position()[0] + other.get_thickness() > self.get_position()[0] >= other.get_position()[0] or \
                other.get_position()[0] < self.get_position()[0] + self.get_thickness() < other.get_position()[
                0] + other.get_thickness():
            if other.get_position()[1] + other.get_thickness() > self.get_position()[1] > other.get_position()[1]:
                return True
            elif other.get_position()[1] + other.get_thickness() >= self.get_position()[1] + self.get_thickness() > \
                    other.get_position()[1]:
                return True
        else:
            return False
