import pygame
pygame.init()


screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Music Player")

player_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab7\\images\\mimimamamu.jpeg")
music = pygame.mixer.Sound("C:\\Users\\Admin\\Desktop\\pp2\\lab7\\song\\mimimamamu.mp3")
music1 = pygame.mixer.Sound("C:\\Users\\Admin\\Desktop\\pp2\\lab7\\song\\backinblack.mp3")
music2 = pygame.mixer.Sound("C:\\Users\\Admin\\Desktop\\pp2\\lab7\\song\\ledzeppelin.mp3")
music_list = [music, music1, music2]

player_rect = player_img.get_rect(center=(700/2, 500/2))

current_music_index = 0
channel = pygame.mixer.Channel(0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if channel.get_busy():
                    channel.pause()
                else:
                    channel.unpause()
            elif event.key == pygame.K_RIGHT:
                current_music_index = (current_music_index + 1) % len(music_list)
                channel.stop()
                channel.play(music_list[current_music_index])
            elif event.key == pygame.K_LEFT:
                current_music_index = (current_music_index - 1) % len(music_list)
                channel.stop()  
                channel.play(music_list[current_music_index])


    screen.fill((255, 255, 255))
    screen.blit(player_img, player_rect)
    pygame.display.flip()

pygame.quit()
