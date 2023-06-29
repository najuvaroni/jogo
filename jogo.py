import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
BRANCO = (255, 255, 255)








PRETO = (0, 0, 0)

# Definição da largura e altura da janela do jogo
largura_tela = 800
altura_tela = 600

# Criação da janela do jogo
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Nick Fast")

class Carro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("carro2.png").convert()
        self.image.set_colorkey(PRETO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_x = 0

    def update(self):
        self.rect.x += self.velocidade_x

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > largura_tela:
            self.rect.right = largura_tela

# Classe para representar os obstáculos
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 5
        if self.rect.top > altura_tela:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, largura_tela - self.rect.width)

# Criação de todos os sprites
todos_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

# Criação do jogador (carro)
carro = Carro(largura_tela // 2, altura_tela - 100)
todos_sprites.add(carro)
for i in range(10):
    obstaculo = Obstaculo(random.randrange(0, largura_tela),
                          random.randrange(-300, -20),
                          random.randrange(20, 100),
                          random.randrange(20, 100),
                          PRETO)
    obstaculos.add(obstaculo)
    todos_sprites.add(obstaculo)

# Criação do relógio para controlar a atualização do jogo
clock = pygame.time.Clock()

terminou = False
pontuacao = 0  # Variável para armazenar a pontuação do jogador

while not terminou:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminou = True

        # Movimentação do carro
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                carro.velocidade_x = -5
            elif evento.key == pygame.K_RIGHT:
                carro.velocidade_x = 5

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT and carro.velocidade_x < 0:
                carro.velocidade_x = 0
            elif evento.key == pygame.K_RIGHT and carro.velocidade_x > 0:
                carro.velocidade_x = 0

    # Atualização do jogo
    todos_sprites.update()

    # Verificação de colisão entre o carro e os obstáculos
    if pygame.sprite.spritecollide(carro, obstaculos, False):
        terminou = True

    # Incrementa a pontuação do jogador a cada frame
    pontuacao += 1

    # Preenchimento do fundo
    tela.fill(BRANCO)

    # Desenho dos sprites na tela
    todos_sprites.draw(tela)

    # Exibe a pontuação na tela
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render("Pontuação: " + str(pontuacao), True, PRETO)
    tela.blit(texto, (10, 10))

    # Atualização da tela
    pygame.display.flip()

    # Definição da taxa de frames por segundo (FPS)
    clock.tick(60)

# Exibe a pontuação final e o nome do jogo
print("Pontuação final: " + str(pontuacao))
print("Nome do Jogo: Nick Fast")

# Encerramento do Pygame
pygame.quit()
