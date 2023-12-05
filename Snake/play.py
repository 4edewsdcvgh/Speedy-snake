# importing libraries
import pygame
import sys
from pygame.math import Vector2
import time
import random

#going to split background into a kinda grid and make snake a list of coords
def play():

    #making images for fruit+bomb
    bomb = pygame.image.load('Assets/snake_graphics/Graphics/bomb.png')
    orange = pygame.image.load('Assets/snake_graphics/Graphics/orange.png')
    lemon = pygame.image.load('Assets/snake_graphics/Graphics/lemon.png')
    apple = pygame.image.load('Assets/snake_graphics/Graphics/apple.png')

    #making snake class
    class Snake:
        def __init__(self):
            self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
            self.direction = Vector2(1, 0)
            self.new_bod = False
            self.head_right = pygame.image.load('Assets/snake_graphics/Graphics/head_right.png')
            self.head_left = pygame.image.load('Assets/snake_graphics/Graphics/head_left.png')
            self.head_up = pygame.image.load('Assets/snake_graphics/Graphics/head_up.png')
            self.head_down = pygame.image.load('Assets/snake_graphics/Graphics/head_down.png')
            self.snake_body = pygame.image.load('Assets/snake_graphics/Graphics/snakebody.png')
            self.snake_tail = pygame.image.load('Assets/snake_graphics/Graphics/snakebody.png')
            self.default_speed = 1.0
            self.speed = self.default_speed

        # increases speed with fruit
        def increase_speed(self, amount):
            self.speed += amount

        #resets speed with bomb
        def reset_speed(self):
            self.speed = self.default_speed  # Reset speed to default

        #drawing snake and making it fit in grid with the cell size
        def draw_snake(self):
            self.update_head_pic()
            self.update_tail_pic()
            for index, block in enumerate(self.body):
                x_pos = int(block.x * c_size)
                y_pos = int(block.y * c_size)
                body_rect = pygame.Rect(x_pos, y_pos, c_size, c_size)

                if index == 0:
                    #snake head
                    screen.blit(self.head, body_rect)
                elif index == len(self.body) - 1:
                    #snake tail
                    screen.blit(self.tail, body_rect)
                else:
                    #body of snake
                    previous_block = self.body[index +1] - block
                    next_block = self.body[index -1] - block

                    #making body when turning
                    if previous_block.x == next_block.x:
                        screen.blit(self.snake_body, body_rect)
                    elif previous_block.y == next_block.y:
                        screen.blit(self.snake_body, body_rect)
                    else:
                        if previous_block.x == -1 and next_block.y ==-1 or previous_block.y == -1 and next_block.x ==-1:
                            screen.blit(self.snake_body,body_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.snake_body,body_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.snake_body,body_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.snake_body,body_rect)

        def update_head_pic(self):
            #math to get snake to move, adding head vector to vector related to keystroke
            head_relate = self.body[1] - self.body[0]
            if head_relate == Vector2(1, 0):
                self.head = self.head_left
            elif head_relate == Vector2(-1, 0):
                self.head = self.head_right
            elif head_relate == Vector2(0, 1):
                self.head = self.head_up
            elif head_relate == Vector2(0, -1):
                self.head = self.head_down

        def update_tail_pic(self):
            #same as above
            tail_relate = self.body[-2] - self.body[-1]
            if tail_relate == Vector2(1, 0):
                self.tail = self.snake_tail
            elif tail_relate == Vector2(-1, 0):
                self.tail = self.snake_tail
            elif tail_relate == Vector2(0, 1):
                self.tail = self.snake_tail
            elif tail_relate == Vector2(0, -1):
                self.tail = self.snake_tail

        #adding snake body part
        def move_snake(self):
            if self.new_bod:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_bod = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]

        #adding
        def add_bod(self):
            self.new_bod = True

    # making the fruit class
    # had to look up pygame.math to find vector (will be using for math)
    # storing x/y into 2d vector (had to look up, vectors allow us to change x and y coord easily)

    class Fruit():
        def __init__(self):
            self.randomize()

        def draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.pos.x * c_size), int(self.pos.y * c_size), c_size, c_size)
            if self.fruit_type == 'apple':
                screen.blit(apple, fruit_rect)
            elif self.fruit_type == 'orange':
                screen.blit(orange, fruit_rect)
            elif self.fruit_type == 'lemon':
                screen.blit(lemon, fruit_rect)
            elif self.fruit_type == 'bomb':
                screen.blit(bomb, fruit_rect)

        def randomize(self):
            #making a random vector for fruits to spawn
            self.x = random.randint(0, c_num -1)
            self.y = random.randint(0, c_num -1)
            self.pos = Vector2(self.x, self.y)
            #list of fruits to spawn
            self.fruit_type = random.choice(['apple', 'orange', 'lemon', 'bomb'])

        #powerups class gives speed
        def powerups(self, snake):
            if self.fruit_type == 'apple':
                pass
            elif self.fruit_type == 'orange':
                snake.increase_speed(0.2)
            elif self.fruit_type == 'lemon':
                snake.increase_speed(0.1)
            elif self.fruit_type == 'bomb':
                snake.reset_speed()

    class Game:
        def __init__(self):
            self.snake = Snake()
            self.fruits = []
            self.spawn_fruits(5)

        #changes list of fruits above
        def spawn_fruits(self, num_fruits):
            for _ in range(num_fruits):
                new_fruit = Fruit()
                self.fruits.append(new_fruit)

        def update(self):
            self.snake.move_snake()
            self.check_game_over()
            self.check_fruit_collision()
            self.check_same_spot()

        def draw_stuff(self):
            self.draw_grass()
            self.snake.draw_snake()
            self.draw_score()
            for fruit in self.fruits:
                fruit.draw_fruit()

        def check_fruit_collision(self):
            snake_head_pos = self.snake.body[0]

            for fruit in self.fruits:
                if snake_head_pos == fruit.pos:
                    fruit.powerups(self.snake)
                    self.fruits.remove(fruit)
                    self.snake.add_bod()
                    new_fruit = Fruit()
                    self.fruits.append(new_fruit)

        def check_same_spot(self):
            for fruit in self.fruits:
                if fruit.pos in self.snake.body:
                    fruit.randomize()

        def check_game_over(self):
            #snake head leaves screen, since vector need to check x/y of head
            if not 0 <= self.snake.body[0].x < c_num or not 0 <= self.snake.body[0].y < c_num:
                self.game_over()

            for bod in self.snake.body[1:]:
                if bod == self.snake.body[0]:
                    self.game_over()
            #snake head hits itself

        def game_over(self):
            pygame.quit()
            sys.exit()

        def draw_grass(self):
            #making board appear to be grid, taking even and odd parts and changing color
            grass_color = (160, 200, 61)
            for r in range(c_num):
                if r % 2 == 0:
                    for c in range(c_num):
                        if c % 2 == 0:
                            grass_rect = pygame.Rect(c * c_size, r * c_size , c_size, c_size)
                            pygame.draw.rect(screen, grass_color, grass_rect)
                else:
                    for c in range(c_num):
                        if c % 2 != 0:
                            grass_rect = pygame.Rect(c * c_size, r * c_size, c_size, c_size)
                            pygame.draw.rect(screen, grass_color, grass_rect)

        #gettign score to appear on screen
        def draw_score(self):
            score_text = str(len(self.snake.body) - 3)
            score_surface = font.render(score_text, True, (56, 74, 12))
            score_x = int(c_size * c_num - 60)
            score_y = int(c_size * c_num - 40)
            score_rect = score_surface.get_rect(center=(score_x, score_y))
            screen.blit(score_surface, score_rect)



    #setting up pygame stuff
    pygame.init()
    c_size = 20
    c_num = 30
    screen = pygame.display.set_mode((c_num * c_size, c_num * c_size))
    clock = pygame.time.Clock()
    font = pygame.font.Font("Assets/Fonts/robot-9000-font/Robot9000-MVxZx.ttf", 28)
    game = Game()

    #making timer to move snake
    screen_update = pygame.USEREVENT
    #triggers event to happen every 100 ms
    pygame.time.set_timer(screen_update, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == screen_update:
               game.update()
            #adding user input
            # prevents double movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game.snake.direction.y != 1:
                        game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if game.snake.direction.y != -1:
                        game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if game.snake.direction.x != -1:
                        game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if game.snake.direction.x != 1:
                        game.snake.direction = Vector2(-1, 0)
        screen.fill((175, 215, 70))
        game.draw_stuff()
        pygame.display.update()
        clock.tick(60)

