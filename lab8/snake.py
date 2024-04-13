import pygame
import sys
import time
import random

pygame.init()

# Color palette
colorBLACK = (0, 0, 0)
colorGRAY = (200, 200, 200)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

WIDTH = 600
HEIGHT = 600
font = pygame.font.SysFont("Verdana", 60)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

score = 0
level = 1
FPS = 5
clock = pygame.time.Clock()
snake_speed = FPS
CELL = 30

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.speed = FPS
        self.level = 1
        

        

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        for segment in self.body[1:]:
            if segment.x == self.body[0].x and segment.y == self.body[0].y:
                game_over_text = font.render("Game Over", True, colorWHITE)
                text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.fill(colorBLACK)
                screen.blit(game_over_text, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)
                done = True
                time.sleep(1)
                pygame.quit()
                sys.exit()

        # Check if snake hits the boundaries
        if self.body[0].x < 0:
            self.body[0].x = 0
            game_over_text = font.render("Game Over", True, colorWHITE)
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.fill(colorBLACK)
            screen.blit(game_over_text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            done = True
            time.sleep(1)
            pygame.quit()
            sys.exit()
        elif self.body[0].x >= WIDTH // CELL:
            self.body[0].x = (WIDTH // CELL) - 1
            game_over_text = font.render("Game Over", True, colorWHITE)
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.fill(colorBLACK)
            screen.blit(game_over_text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            done = True
            time.sleep(1)
            pygame.quit()
            sys.exit()
        if self.body[0].y < 0:
            self.body[0].y = 0 
            game_over_text = font.render("Game Over", True, colorWHITE)
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.fill(colorBLACK)
            screen.blit(game_over_text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            done = True
            time.sleep(1)
            pygame.quit()
            sys.exit()
        elif self.body[0].y >= HEIGHT // CELL:
            self.body[0].y = (HEIGHT // CELL) - 1
            game_over_text = font.render("Game Over", True, colorWHITE)
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.fill(colorBLACK)
            screen.blit(game_over_text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            done = True
            time.sleep(1)
            pygame.quit()
            sys.exit()

        

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.generate_new_position()
            global score
            score += 1
            if score % 10 == 0 and score != 0:
                self.level += 1
                self.speed += 5
            return True
        return False
    
    def draw_score(self):
        score_font = pygame.font.SysFont("Verdana", 20)
        score_text = score_font.render("Score: " + str(score), True, colorBLACK)
        screen.blit(score_text, (0, 0))

    def draw_level(self):
        level_font = pygame.font.SysFont("Verdana", 20)
        level_text = level_font.render("Level: " + str(self.level), True, colorBLACK)
        screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 0))
        
class Food:
    def __init__(self):
        self.pos = Point(15, 15)

    def generate_new_position(self):
        new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        while new_pos in snake.body:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.pos = new_pos

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

done = False

snake = Snake()
food = Food()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
    draw_grid_chess()

    snake.move()
    snake.draw()
    snake.draw_score()
    snake.draw_level()
    

    food.draw()

    if snake.check_collision(food):
        print("Got food!")

    
    pygame.display.flip()
    clock.tick(snake.speed)
    
