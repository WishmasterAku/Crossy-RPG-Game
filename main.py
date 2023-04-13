import pygame

pygame.init()

#######Game Code########
width = 800
height = 899
background_color = "black"
game_window = pygame.display.set_mode((width, height))
game_window.fill(background_color)  
pygame.display.update()


pygame.quit()
quit()