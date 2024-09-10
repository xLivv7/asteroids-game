import pygame
from shot import *
from constants import *
from circleshape import *
class Player(CircleShape):
    containers = None   
    

    def __init__(self,x,y):
        if Player.containers:
            pygame.sprite.Sprite.__init__(self, self.containers)
        self.position = pygame.Vector2(x,y)
        super().__init__( self.position.x, self.position.y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
   
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation +=(PLAYER_TURN_SPEED*dt)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        self.timer -= dt
        if self.timer < 0:
                self.timer = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, shot_velocity)