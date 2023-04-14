import pygame

pygame.init()

#######Game Code########
width = 800
height = 800
background_color = "black"
game_window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

while True:
    game_window.fill(background_color)  
    pygame.display.update()
    
    clock.tick(60)
    

pygame.quit()
quit()