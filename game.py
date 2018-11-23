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
        # window related stuff
        self.window_height = 600
        self.window_width = 800
        self.playfield_height = self.window_height - 100
        self.playfield_width = self.window_width
        self.window_caption = "Slither.ie"
        self.hud_color = self.BLACK

        # game related stuff
        self.fps = 15
        self.block_size = 20
        self.player_score = 0
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
        self.snake_head_sprite = None

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
            # todo draw whole snake
            self.draw_apple()
            self.draw_player()
            self.display_player_score()
            pygame.display.update()
            self.game_clock.tick(self.fps)

        pygame.quit()
        quit(0)

    def draw_screen(self):
        self.game_window.fill(self.hud_color)
        pygame.draw.rect(self.game_window, self.LIGHT_GREY, [0, 50, self.playfield_width, self.playfield_height])

    def display_player_score(self):
        score_string = "Score: " + str(self.player_score)
        text_surface = self.text_font.render(score_string, True, self.WHITE)
        # text_surface.get_rect().center = (self.window_width / 2), 10
        self.game_window.blit(text_surface, text_surface.get_rect())

    def load_sprites(self):
        self.snake_head_sprite = pygame.image.load("assets/snake_head.png")

    def process_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.key == pygame.K_ESCAPE:
                    self.game_over = True
                # LEFT
                if event.key == pygame.K_LEFT:
                    self.snake.direction = "left"
                # RIGHT
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = "right"
                # UP
                elif event.key == pygame.K_UP:
                    self.snake.direction = "up"
                # DOWN
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = "down"

    def spawn_new_apple(self):
        self.apple = Apple([0, self.playfield_width], [50, self.playfield_height + 50], self.block_size)

    def draw_apple(self):
        pygame.draw.rect(self.game_window, self.apple_color, self.apple.get_position_thickness_thickness())

    def spawn_player(self):
        self.snake = Snake([0, self.playfield_width], [50, self.playfield_height + 50], self.block_size, self.block_size)

    def draw_player(self):
        self.game_window.blit(self.snake_head_sprite, [self.snake.get_x_position(), self.snake.get_y_position()])

    def check_collisions(self):
        if self.snake.collides_with(self.apple):
            self.apple.is_eaten = True
            self.player_score += 1
            print("{} ate {}".format(str(self.snake), str(self.apple)))

    def calculate_frame(self):
        self.snake.move()


this = Game()
