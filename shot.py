import pygame
from constants import *
from circleshape import *
from main import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen,"yellow",self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt