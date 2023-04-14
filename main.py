import pygame

pygame.init()

#######Game Code########
width = 800
height = 800
background_color = "black"
game_window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()#set clock

background_image = pygame.image.load('assets/assets/background.png')#load image
background = pygame.transform.scale(background_image, (width, height))#resize image
treasure_image = pygame.image.load('assets/assets/treasure.png')
treasure = pygame.transform.scale(treasure_image, (50, 50))

def run_game():
    while True:
        events = pygame.event.get()#get all events
        for event in events:
            if event.type == pygame.QUIT:#if user clicks close
                return

        game_window.fill(background_color)  

        game_window.blit(background, (0, 0))#Top Left Corner | 800 x 800 = Bottom Right Corner
        game_window.blit(treasure, (375, 50))


        
        pygame.display.update()        
        clock.tick(60)#set fps



run_game()
pygame.quit()
quit()