import pygame

class Game:

    def __init__(self):

        self.width = 800
        self.height = 800
        self.background_color = "black"
        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()#set clock

        background_image = pygame.image.load('assets/assets/background.png')#load image
        self.background = pygame.transform.scale(background_image, (self.width, self.height))#resize image
        treasure_image = pygame.image.load('assets/assets/treasure.png')
        self.treasure = pygame.transform.scale(treasure_image, (50, 50))

    def draw_objects(self):
        self.game_window.fill(self.background_color)  
        self.game_window.blit(self.background, (0, 0))#Top Left Corner | 800 x 800 = Bottom Right Corner
        self.game_window.blit(self.treasure, (380, 50))            
        pygame.display.update()   

    def run_game(self):#Method that belongs to Game Class so needs Self init to access variables
        while True:
            events = pygame.event.get()#get all events
            for event in events:
                if event.type == pygame.QUIT:#if user clicks close
                    return

            self.draw_objects()

            self.clock.tick(60)#set fps