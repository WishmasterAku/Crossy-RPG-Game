import pygame
from gameObjects import GameObject

class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):#init is a method that is called when an object is created from a class
        super().__init__(x, y, width, height, image_path)#super() is used to inherit from parent class

        self.speed = speed

       

    def move(self, direction, max_height):
        if (self.y >= max_height - self.height and direction > 0) or (self.y == 0 and direction < 0):#if player is at top or bottom of screen
            return

        self.y += (direction * self.speed)

    
        