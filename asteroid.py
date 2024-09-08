import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,velocity=pygame.Vector2(0,0)):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity *dt


        