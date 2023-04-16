import pygame
from gameObjects import GameObject
from player import Player
from enemy import Enemy

class Game:

    def __init__(self):

        self.width = 800
        self.height = 800
        self.background_color = "black"
        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.player = Player(375, 700, 50, 50, 'assets/assets/player.png', 10)
        self.clock = pygame.time.Clock()#set clock

        self.background = GameObject(0, 0, self.width, self.height, 'assets/assets/background.png')
        self.player = Player(375, 700, 50, 50, 'assets/assets/player.png', 2)
        self.treasure = GameObject(375, 50, 50, 50, 'assets/assets/treasure.png')

        self.enemy = Enemy(50, 400, 50, 50, 'assets/assets/enemy.png', 5)

        

    def draw_objects(self):
        self.game_window.fill(self.background_color)  

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))#Top Left Corner | 800 x 800 = Bottom Right Corner
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))       
        self.game_window.blit(self.enemy.image, (self.enemy.x, self.enemy.y))

        pygame.display.update()   

    def detect_collsion(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        
        return True


    def run_game(self):#Method that belongs to Game Class so needs Self init to access variables

        player_direction = 0

        while True: #Handle events
            events = pygame.event.get()#get all events
            for event in events:
                if event.type == pygame.QUIT:#if user clicks close
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #Move player up
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        #Move player down
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0


            # Execute Logic
            self.player.move(player_direction, self.height)
            self.enemy.move(self.width)


            self.draw_objects()

            # Check for collisions
            if self.detect_collsion(self.player, self.enemy):
                return
            elif self.detect_collsion(self.player, self.treasure):
                return

            self.clock.tick(60)#set fps