import movableGameObject
import gameObject

print(isinstance(1, int))
my_apple = gameObject.GameObject([0, 200], [0, 150], 20)
print(my_apple.get_thickness())
print(my_apple.get_position())

my_snake = movableGameObject.MovableGameObject(100, 200, 20, 2000, 2000, 20)
print(my_snake.get_thickness())
print(my_snake.get_position())
print(my_snake.collides_with(my_snake))
