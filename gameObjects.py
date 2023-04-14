import pygame

class GameObject:#Class for all objects in game. All objects will need a x, y, width, height, image_path

    def __init__(self, x, y, width, height, image_path):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    