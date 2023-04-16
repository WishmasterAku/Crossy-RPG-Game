import pygame
from gameObjects import GameObject

class Enemy(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):#init is a method that is called when an object is created from a class
        super().__init__(x, y, width, height, image_path)#super() is used to inherit from parent class

        self.speed = speed

       

    def move(self, max_width):
        if self.x <= 0 + 150:
            self.speed = abs(self.speed)#abs() returns the absolute value of a number
        elif self.x >= max_width - 150:
            self.speed = -self.speed



        self.x += self.speed