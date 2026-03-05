import pygame
import math
import random

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
    "   W.W       W.W    ",
    "WWWW.W WWWWW W.WWWW",
    "S    f       f    S",
    "WWWW.W WWWWW W.WWWW",
    "   W.W       W.W    ",
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
        # IA Simples: Segue reto até bater, depois escolhe nova direção
        next_rect = self.rect.move(self.dir[0] * self.vel, self.dir[1] * self.vel)
        if next_rect.collidelist(walls) != -1:
            self.dir = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        else:
            self.rect = next_rect

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        
        # Inicializar Mixer para sons
        pygame.mixer.init()
        
        self.walls = []
        self.dots = []
        self.ghosts = []
        self.player_rect = None
        
        self.load_map()

    def load_map(self):
        for row, line in enumerate(MAP):
            for col, char in enumerate(line):
                if char == "W":
                    self.walls.append(pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif char == ".":
                    self.dots.append(pygame.Rect(col*TILE_SIZE + 12, row*TILE_SIZE + 12, 6, 6))
                elif char == "S":
                    self.player_rect = pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE-4, TILE_SIZE-4)
                elif char == "f":
                    self.ghosts.append(Ghost(col, row, (255, 0, 100)))

    def play_chomp(self):
        # Gera um som de "beep" curto simulando o comer
        try:
            s = pygame.mixer.Sound(buffer=bytes([random.randint(0, 255) for _ in range(500)]))
            s.set_volume(0.1)
            s.play()
        except: pass

    def run(self):
        while self.running:
            self.screen.fill((5, 5, 15)) # Fundo Dark Blue
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Movimentação com Colisão
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT]: dx = -3
            elif keys[pygame.K_RIGHT]: dx = 3
            elif keys[pygame.K_UP]: dy = -3
            elif keys[pygame.K_DOWN]: dy = 3

            # Teste de colisão X e Y separados para deslizar nas paredes
            new_rect = self.player_rect.move(dx, 0)
            if new_rect.collidelist(self.walls) == -1:
                self.player_rect = new_rect
            
            new_rect = self.player_rect.move(0, dy)
            if new_rect.collidelist(self.walls) == -1:
                self.player_rect = new_rect

            # Comer pontos
            for dot in self.dots[:]:
                if self.player_rect.colliderect(dot):
                    self.dots.remove(dot)
                    self.score += 10
                    self.play_chomp()

            # Desenhar Paredes Neon
            for wall in self.walls:
                pygame.draw.rect(self.screen, (0, 150, 255), wall, 1, border_radius=3)

            # Desenhar Pontos
            for dot in self.dots:
                pygame.draw.circle(self.screen, (255, 255, 255), dot.center, 3)

            # Atualizar e Desenhar Fantasmas
            for g in self.ghosts:
                g.update(self.walls)
                pygame.draw.ellipse(self.screen, g.color, g.rect)
                if self.player_rect.colliderect(g.rect):
                    print("Game Over!")
                    self.running = False

            # Desenhar Player (Boca animada simples)
            angle = (pygame.time.get_ticks() // 100) % 2 * 30
            pygame.draw.pie(self.screen, (255, 255, 0), self.player_rect, math.radians(angle), math.radians(360-angle))

            # HUD
            font = pygame.font.SysFont("Verdana", 20, bold=True)
            txt = font.render(f"PONTOS: {self.score}", True, (255, 255, 255))
            self.screen.blit(txt, (10, 5))

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()
    pygame.quit()
