import pygame
import random

# this is a test string..
def snake(snake_list, direction, snake_head_img):
    if direction == "right":
        snake_head_img_rotated = pygame.transform.rotate(snake_head_img, 270)
    elif direction == "left":
        snake_head_img_rotated = pygame.transform.rotate(snake_head_img, 90)
    elif direction == "up":
        snake_head_img_rotated = snake_head_img
    elif direction == "down":
        snake_head_img_rotated = pygame.transform.rotate(snake_head_img, 180)

    game_display.blit(snake_head_img_rotated, (snake_list[-1][0], snake_list[-1][1]))

    for x_y in snake_list[:-1]:
        pygame.draw.ellipse(game_display, green, [x_y[0], x_y[1], block_size, block_size])


def message_to_screen(msg, color):
    text_surface = font.render(msg, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (window_width / 2), (window_height / 2)
    game_display.blit(text_surface, text_rect)


def game_loop():
    game_exit = False
    game_over = False


    lead_x_change = 10
    lead_y_change = 0

    while not game_exit:

        while game_over:
            game_display.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit.", green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False

                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            # press the close button
            if event.type == pygame.QUIT:
                game_exit = True

            # key presses
            if event.type == pygame.KEYDOWN:
                # ESC
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                # LEFT
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    snake_direction = "left"
                # RIGHT
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    snake_direction = "right"
                # UP
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    snake_direction = "up"
                # DOWN
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    snake_direction = "down"

        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x >= window_width:
            lead_x = 0

        if lead_x < 0:
            lead_x = window_width

        if lead_y >= window_height:
            lead_y = 0

        if lead_y < 0:
            lead_y = window_height

        # draw background
        game_display.fill(black)

        apple_thickness = block_size + 20

        # calculate collisions
        if rand_apple_x + apple_thickness > lead_x >= rand_apple_x or rand_apple_x < lead_x + block_size < rand_apple_x + apple_thickness:
            if rand_apple_y + apple_thickness > lead_y > rand_apple_y:
                rand_apple_x = round(random.randrange(0, window_width - block_size) / block_size) * block_size
                rand_apple_y = round(random.randrange(0, window_height - block_size) / block_size) * block_size
                snake_length += 1

            elif rand_apple_y + apple_thickness >= lead_y + block_size > rand_apple_y:
                rand_apple_x = round(random.randrange(0, window_width - block_size) / block_size) * block_size
                rand_apple_y = round(random.randrange(0, window_height - block_size) / block_size) * block_size
                snake_length += 1

        # draw apple
        pygame.draw.rect(game_display, red, [rand_apple_x, rand_apple_y, apple_thickness, apple_thickness])

        # draw player
        snake_head = []

        snake_head.append(lead_x)
        snake_head.append(lead_y)

        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        snake(snake_list, snake_direction, snake_head_img)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()


game_loop()
