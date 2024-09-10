import pygame
import random
from constants import *
from circleshape import *
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,velocity=pygame.Vector2(0,0)):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity *dt

    def split(self, radius):
        self.kill()
        if radius <= ASTEROID_MIN_RADIUS:
            return None
        else:
            rand_angle = random.uniform(20,50)
            neg_rand_angle = self.velocity.rotate(-rand_angle)
            pos_rand_angle = self.velocity.rotate(rand_angle)
            new_radius = radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, pos_rand_angle * 1.2)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, neg_rand_angle * 1.2)
        