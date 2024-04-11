import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640

# Color palette
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define color rectangles
color_rectangles = [
    pygame.Rect(10, 10, 30, 30),  # Black
    pygame.Rect(50, 10, 30, 30),  # White
    pygame.Rect(90, 10, 30, 30),  # Red
    pygame.Rect(130, 10, 30, 30), # Green
    pygame.Rect(170, 10, 30, 30), # Blue
    pygame.Rect(210, 10, 80, 30)  # Eraser
]

# Define corresponding colors
colors = [
    colorBLACK,
    colorWHITE,
    colorRED,
    colorGREEN,
    colorBLUE,
    colorBLACK  # Eraser color (Black)
]

# Define texts
font = pygame.font.SysFont(None, 24)
eraser_text = font.render("Eraser", True, colorWHITE)

done = False
LMBpressed = False
prevX = 0
prevY = 0
currX = 0
currY = 0
selected_color = colorYELLOW

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if color rectangle clicked
            for i, rect in enumerate(color_rectangles):
                if rect.collidepoint(event.pos):
                    selected_color = colors[i]
                    break

            LMBpressed = True

        if event.type == pygame.MOUSEMOTION:
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False

    if LMBpressed:
        # If selected color is the eraser color, use it to erase
        if selected_color == colors[-1]:
            pygame.draw.line(screen, selected_color, (prevX, prevY), (currX, currY), 20) # Use thick line to erase
        else:
            pygame.draw.line(screen, selected_color, (prevX, prevY), (currX, currY))

    prevX = currX
    prevY = currY

    # Draw color rectangles
    for i, rect in enumerate(color_rectangles):
        pygame.draw.rect(screen, colors[i], rect)
        if i == len(color_rectangles) - 1:
            screen.blit(eraser_text, (220, 17))

    pygame.display.flip()
