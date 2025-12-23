from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import pygame, random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        pos_vector = self.velocity.rotate(random_angle)
        neg_vector = self.velocity.rotate(-1 * random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = pos_vector * 1.2
        asteroid2.velocity = neg_vector * 1.2
