import pygame

from constants import *
from circleshape import *
class Player(CircleShape):
    def __init__(self,x,y):
        self.position = pygame.Vector2(x,y)
        super().__init__( self.position.x, self.position.y, PLAYER_RADIUS)
        self.rotation = 0
   
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
