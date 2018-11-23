from gameObject import GameObject


class Apple(GameObject):
    def __init__(self, x_range, y_range, thickness):
        super().__init__(x_range, y_range, thickness)
        self.is_eaten = False
