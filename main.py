import pygame

pygame.init()

#######Game Code########
width = 800
height = 800
background_color = "black"
game_window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()#set clock

def run_game():
    while True:
        events = pygame.event.get()#get all events
        for event in events:
            if event.type == pygame.QUIT:#if user clicks close
                return

        game_window.fill(background_color)  
        pygame.display.update()
        
        clock.tick(60)#set fps

run_game()
pygame.quit()
quit()