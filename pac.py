import pygame
import math
import random
import sys

# Configurações do Jogo
TILE_SIZE = 30
MAP = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W........W.........W",
    "W.WW.WWW.W.WWW.WW.W",
    "W..................W",
    "W.WW.W.WWWWW.W.WW.W",
    "W....W...W...W....W",
    "WWWW.WWW W WWW.WWWW",
    "    W.W       W.W    ",
    "WWWW.W WWWWW W.WWWW",
    "S    f       f    S",
    "WWWW.W WWWWW W.WWWW",
    "    W.W       W.W    ",
    "WWWW.W WWWWW W.WWWW",
    "W........W.........W",
    "W.WW.WWW.W.WWW.WW.W",
    "W..W...........W..W",
    "WW.W.W.WWWWW.W.W.WW",
    "W....W...W...W....W",
    "W.WWWWWW.W.WWWWWW.W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

WIDTH = len(MAP[0]) * TILE_SIZE
HEIGHT = len(MAP) * TILE_SIZE

class Ghost:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE-4, TILE_SIZE-4)
        self.color = color
        self.vel = 2
        self.dir = random.choice([(0,1), (0,-1), (1,0), (-1,0)])

    def update(self, walls):
        next_rect = self.rect.move(self.dir[0] * self.vel, self.dir[1] * self.vel)
        if next_rect.collidelist(walls) != -1:
            self.dir = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        else:
            self.rect = next_rect

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Neon-Man")
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        
        self.walls = []
        self.dots = []
        self.ghosts = []
        self.player_rect = None
        
        self.load_map()

    def load_map(self):
        for row, line in enumerate(MAP):
            for col, char in enumerate(line):
                x, y = col * TILE_SIZE, row * TILE_SIZE
                if char == "W":
                    self.walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
                elif char == ".":
                    self.dots.append(pygame.Rect(x + 12, y + 12, 6, 6))
                elif char == "S":
                    self.player_rect = pygame.Rect(x, y, TILE_SIZE-4, TILE_SIZE-4)
                elif char == "f":
                    self.ghosts.append(Ghost(col, row, (255, 50, 50)))

    def run(self):
        while self.running:
            self.screen.fill((10, 10, 30))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT]: dx = -3
            elif keys[pygame.K_RIGHT]: dx = 3
            elif keys[pygame.K_UP]: dy = -3
            elif keys[pygame.K_DOWN]: dy = 3

            # Movimento com colisão
            old_pos = self.player_rect.copy()
            self.player_rect.x += dx
            if self.player_rect.collidelist(self.walls) != -1:
                self.player_rect.x = old_pos.x
            
            self.player_rect.y += dy
            if self.player_rect.collidelist(self.walls) != -1:
                self.player_rect.y = old_pos.y

            # Comer pontos
            self.dots = [d for d in self.dots if not self.player_rect.colliderect(d)]
            self.score = (len(MAP[0]*len(MAP)) - len(self.dots)) # Score simples

            # Desenhar
            for wall in self.walls:
                pygame.draw.rect(self.screen, (0, 200, 255), wall, 1, border_radius=5)
            for dot in self.dots:
                pygame.draw.circle(self.screen, (255, 255, 255), dot.center, 2)
            for g in self.ghosts:
                g.update(self.walls)
                pygame.draw.ellipse(self.screen, g.color, g.rect)
                if self.player_rect.colliderect(g.rect):
                    self.running = False

            # Player
            pygame.draw.ellipse(self.screen, (255, 255, 0), self.player_rect)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()
    pygame.quit()
