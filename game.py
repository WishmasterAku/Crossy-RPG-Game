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
        
        self.treasure = GameObject(375, 50, 50, 50, 'assets/assets/treasure.png')
        
        self.level = 1.0

        self.reset_map()
    
    def reset_map(self):
        self.player = Player(375, 700, 50, 50, 'assets/assets/player.png', 3)

        speed = 2 + (self.level * 5)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(100, 400, 50, 50, 'assets/assets/enemy.png', speed),
                Enemy(650, 600, 50, 50, 'assets/assets/enemy.png', speed),
                Enemy(550, 300, 50, 50, 'assets/assets/enemy.png', speed),            
                            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(100, 400, 50, 50, 'assets/assets/enemy.png', speed),
                Enemy(650, 600, 50, 50, 'assets/assets/enemy.png', speed),
                            ]
        else:
            self.enemies = [
                Enemy(100, 400, 50, 50, 'assets/assets/enemy.png', speed),
                            ]



    def move_objects(self, player_direction):
            self.player.move(player_direction, self.height)
            for enemy in self.enemies:
                enemy.move(self.width)

        

    def draw_objects(self):
        self.game_window.fill(self.background_color)  

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))#Top Left Corner | 800 x 800 = Bottom Right Corner
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y)) 

        for enemy in self.enemies:      
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()   

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collsion(self.player, enemy):
                self.level = 1.0
                return True
            if self.detect_collsion(self.player, self.treasure):
                self.level += 0.5
                return True
            return False

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
            self.move_objects(player_direction)

            self.draw_objects()

            # Check for collisions
            
            if self.check_if_collided():
                self.reset_map()

            self.clock.tick(60)#set fps