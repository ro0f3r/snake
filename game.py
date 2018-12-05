import pygame
from apple import Apple
from snake import Snake


class Game:
    # define all necessary colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    LIGHT_GREY = (211, 211, 211)

    def __init__(self):
        # window related stufff
        self.window_height = 600
        self.window_width = 800
        self.playfield_height = self.window_height - 100
        self.playfield_width = self.window_width
        self.window_caption = "Slither.ie"
        self.hud_color = self.BLACK

        # game related stuff
        self.fps = 10
        self.block_size = 20
        self.player_score = 0
        self.player_name = "HANSPETER_ÜÄÖ"
        self.game_over = False
        self.apple = None
        self.snake = None
        self.apple_color = self.RED

        # initialize pygame stuff
        pygame.init()
        pygame.display.set_caption("slither.ie")
        self.game_window = pygame.display.set_mode((self.window_width, self.window_height))
        self.game_clock = pygame.time.Clock()
        self.text_font = pygame.font.SysFont(None, 25)

        # "initialize" sprites due to readability
        self.apple_sprite = None
        self.snake_head_sprite = {}
        self.snake_body_sprite = {}

        self.start_game()

    def start_game(self):
        self.load_sprites()
        self.spawn_player()
        self.spawn_new_apple()
        self.draw_screen()

        while not self.game_over:
            # process events
            self.process_events(pygame.event.get())
            self.check_collisions()

            self.calculate_frame()

            # spawn a new apple if the old one got eaten and draw it to the screen
            if self.apple.is_eaten:
                self.spawn_new_apple()

            # update window
            self.draw_screen()
            self.draw_apple()
            self.draw_player()
            self.display_player_score()
            self.display_player_name()
            pygame.display.update()
            self.game_clock.tick(self.fps)

        pygame.quit()
        quit(0)

    def draw_screen(self):
        self.game_window.fill(self.hud_color)
        pygame.draw.rect(self.game_window, self.WHITE, [0, 50, self.playfield_width, self.playfield_height])

    def display_player_score(self):
        score_string = "Score: " + str(self.player_score)
        text_surface = self.text_font.render(score_string, True, self.WHITE)
        # text_surface.get_rect().center = (self.window_width / 2), 10
        self.game_window.blit(text_surface, text_surface.get_rect())

    def display_player_name(self):
        name_string = "Name: " + str(self.player_name)
        text_surface = self.text_font.render(name_string, True, self.WHITE)
        self.game_window.blit(text_surface, (self.window_width - text_surface.get_width(), 0))

    def load_sprites(self):
        # initialize apple sprite
        self.apple_sprite = pygame.image.load("sprites/apple.png")

        # initialize all snake head sprites
        self.snake_head_sprite["up"] = pygame.image.load("sprites/snake_head.png")
        self.snake_head_sprite["left"] = pygame.transform.rotate(self.snake_head_sprite["up"], 90)
        self.snake_head_sprite["down"] = pygame.transform.rotate(self.snake_head_sprite["up"], 180)
        self.snake_head_sprite["right"] = pygame.transform.rotate(self.snake_head_sprite["up"], 270)

        # initialize all snake body sprites
        self.snake_body_sprite["up"] = pygame.image.load("sprites/snake_body.png")
        self.snake_body_sprite["left"] = pygame.transform.rotate(self.snake_body_sprite["up"], 90)
        self.snake_body_sprite["down"] = pygame.transform.rotate(self.snake_body_sprite["up"], 180)
        self.snake_body_sprite["right"] = pygame.transform.rotate(self.snake_body_sprite["up"], 270)

        self.snake_body_sprite["right-down"] = pygame.image.load("sprites/snake_body_turn.png")
        self.snake_body_sprite["up-left"] = self.snake_body_sprite["right-down"]

        self.snake_body_sprite["left-down"] = pygame.transform.rotate(self.snake_body_sprite["right-down"], 90)
        self.snake_body_sprite["up-right"] = self.snake_body_sprite["left-down"]

        self.snake_body_sprite["left-up"] = pygame.transform.rotate(self.snake_body_sprite["right-down"], 180)
        self.snake_body_sprite["down-right"] = self.snake_body_sprite["left-up"]

        self.snake_body_sprite["right-up"] = pygame.transform.rotate(self.snake_body_sprite["right-down"], 270)
        self.snake_body_sprite["down-left"] = self.snake_body_sprite["right-up"]

    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.key == pygame.K_ESCAPE:
                    self.game_over = True
                # LEFT
                if event.key == pygame.K_LEFT:
                    self.snake.head.set_direction("left")
                # RIGHT
                elif event.key == pygame.K_RIGHT:
                    self.snake.head.set_direction("right")
                # UP
                elif event.key == pygame.K_UP:
                    self.snake.head.set_direction("up")
                # DOWN
                elif event.key == pygame.K_DOWN:
                    self.snake.head.set_direction("down")

    def spawn_new_apple(self):
        self.apple = Apple([0, self.playfield_width], [50, self.playfield_height + 50], self.block_size)

    def draw_apple(self):
        self.game_window.blit(self.apple_sprite, self.apple.get_position_thickness_thickness())

    def spawn_player(self):
        self.snake = Snake([0, self.playfield_width], [50, self.playfield_height + 50], self.block_size, self.block_size)

    def draw_player(self):
        if self.snake.head.get_direction() == "up":
            self.game_window.blit(self.snake_head_sprite["up"], self.snake.head.get_position())
        elif self.snake.head.get_direction() == "right":
            self.game_window.blit(self.snake_head_sprite["right"], self.snake.head.get_position())
        elif self.snake.head.get_direction() == "down":
            self.game_window.blit(self.snake_head_sprite["down"], self.snake.head.get_position())
        elif self.snake.head.get_direction() == "left":
            self.game_window.blit(self.snake_head_sprite["left"], self.snake.head.get_position())

        for i in range(len(list(reversed(self.snake.body_parts)))):
            try:
                if self.snake.body_parts[i].get_direction() == "up":
                    if self.snake.body_parts[i + 1].get_direction() == "left":
                        self.game_window.blit(self.snake_body_sprite["up-left"], self.snake.body_parts[i + 1].get_position())
                    elif self.snake.body_parts[i + 1].get_direction() == "right":
                        self.game_window.blit(self.snake_body_sprite["up-right"], self.snake.body_parts[i + 1].get_position())
                    else:
                        self.game_window.blit(self.snake_body_sprite["up"], self.snake.body_parts[i + 1].get_position())

                elif self.snake.body_parts[i].get_direction() == "left":
                    if self.snake.body_parts[i + 1].get_direction() == "down":
                        self.game_window.blit(self.snake_body_sprite["left-down"], self.snake.body_parts[i + 1].get_position())
                    elif self.snake.body_parts[i + 1].get_direction() == "up":
                        self.game_window.blit(self.snake_body_sprite["left-up"], self.snake.body_parts[i + 1].get_position())
                    else:
                        self.game_window.blit(self.snake_body_sprite["left"], self.snake.body_parts[i + 1].get_position())

                elif self.snake.body_parts[i].get_direction() == "down":
                    if self.snake.body_parts[i + 1].get_direction() == "right":
                        self.game_window.blit(self.snake_body_sprite["down-right"], self.snake.body_parts[i + 1].get_position())
                    elif self.snake.body_parts[i + 1].get_direction() == "left":
                        self.game_window.blit(self.snake_body_sprite["down-left"], self.snake.body_parts[i + 1].get_position())
                    else:
                        self.game_window.blit(self.snake_body_sprite["down"], self.snake.body_parts[i + 1].get_position())

                elif self.snake.body_parts[i].get_direction() == "right":
                    if self.snake.body_parts[i + 1].get_direction() == "down":
                        self.game_window.blit(self.snake_body_sprite["right-down"], self.snake.body_parts[i + 1].get_position())
                    elif self.snake.body_parts[i + 1].get_direction() == "up":
                        self.game_window.blit(self.snake_body_sprite["right-up"], self.snake.body_parts[i + 1].get_position())
                    else:
                        self.game_window.blit(self.snake_body_sprite["right"], self.snake.body_parts[i + 1].get_position())
            except IndexError:
                pass

    def check_collisions(self):
        if self.snake.collides_with(self.apple):
            self.snake.length += 1
            self.apple.is_eaten = True
            self.player_score += 1
            print("{} ate {}".format(str(self.snake), str(self.apple)))

        for body_part in self.snake.get_body_parts()[:-1]:
            if self.snake.get_body_parts()[-1].get_position() == body_part.get_position():
                self.game_over = True

    def calculate_frame(self):
        self.snake.move()


this = Game()
