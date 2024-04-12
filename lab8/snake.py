import pygame
import sys
import time
import random

pygame.init()

# color palette
colorBLACK = (0, 0, 0)
colorGRAY = (200, 200, 200)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

WIDTH = 1800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 5
clock = pygame.time.Clock()
SCORE = 0

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
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        # Инициализация змеи с тремя точками тела и начальным направлением движения вправо
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # Изменение координаты x (горизонтальное движение)
        self.dy = 0  # Изменение координаты y (вертикальное движение)

    def move(self):
        # Перемещение тела змеи
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        
        # Перемещение головы змеи в соответствии с текущими dx и dy
        self.body[0].x += self.dx
        self.body[0].y += self.dy
    
    def is_out_of_bounds(self, width, height):
        for segment in self.body:
            if segment.x < 0 or segment.x >= width or segment.y < 0 or segment.y >= height:
                return True
        return False

    def draw(self):
        # Отрисовка головы змеи
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        # Отрисовка остального тела змеи
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        # Проверка столкновения головы змеи с едой
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            # Если столкновение произошло, добавляем новую точку к телу змеи и возвращаем True
            self.body.append(Point(head.x, head.y))
            return True
        return False  # Возвращаем False, если столкновение не произошло


class Food:
    def __init__(self):
        self.pos = Point(15, 15)

    def move(self):
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]

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
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1

    draw_grid_chess()

    snake.move()
    snake.draw()
    snake.is_out_of_bounds(WIDTH, HEIGHT)
    food.draw()

    if snake.check_collision(food):
        print("Got food!")
    
    pygame.display.flip()
    clock.tick(FPS)
