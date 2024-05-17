import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rato em busca de queijo")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Carregar imagens
rat_img = pygame.image.load("rat.png")
cheese_img = pygame.image.load("cheese.png")

# Posições iniciais
rat_x, rat_y = WIDTH // 2, HEIGHT // 2
cheese_x, cheese_y = random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)

# Velocidade do rato
vel = 5

# Loop principal
playing = True
while playing:
    screen.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False

    # Movimento do rato
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rat_x -= vel
    if keys[pygame.K_RIGHT]:
        rat_x += vel
    if keys[pygame.K_UP]:
        rat_y -= vel
    if keys[pygame.K_DOWN]:
        rat_y += vel

    # Verificar colisão com o queijo
    if rat_x < cheese_x + 50 and rat_x + 50 > cheese_x and rat_y < cheese_y + 50 and rat_y + 50 > cheese_y:
        cheese_x, cheese_y = random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)

    # Desenhar rato e queijo
    screen.blit(rat_img, (rat_x, rat_y))
    screen.blit(cheese_img, (cheese_x, cheese_y))

    pygame.display.update()

# Encerrar o Pygame
pygame.quit()
