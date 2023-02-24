import pygame
import random

# Inicializar pygame e configurar tela
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jogo da Cobra")

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define a posição inicial e tamanho da cobra
snake_block = 10
snake_speed = 50
snake_list = []

# Posição inicial da cobra
x1 = 300
y1 = 300

# Direção inicial da cobra
x1_change = snake_block
y1_change = 0

# Posição inicial da maçã
applex = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0
appley = round(random.randrange(0, 300 - snake_block) / 10.0) * 10.0

clock = pygame.time.Clock()

def init_snake(size):
    for i in range(size):
        snake_list.append([x1-i*snake_block, y1])

init_snake(2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    # add the new position of the snake's head to the snake_list
    snake_list.insert(0, [x1, y1])

    # Check if the snake is within the screen
    if x1 >= 800 or x1 < 0 or y1 >= 800 or y1 < 0:
        running = False


    # Desenha o fundo da tela
    screen.fill(black)
    # Desenha a maçã
    pygame.draw.rect(screen, red, [applex, appley, snake_block,snake_block])
    
    # Desenha a cobra
    for x,y in snake_list:
        pygame.draw.rect(screen, white, [x, y, snake_block, snake_block])

    # Verifica se a cobra colidiu com a maçã
    if x1 == applex and y1 == appley:
        applex = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0
        appley = round(random.randrange(0, 300 - snake_block) / 10.0) * 10.0
        # Adiciona um quadrado na frente da cobra
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.insert(0, snake_head)
    else:
        if len(snake_list)>1:
            snake_list.pop()
    # Controla a velocidade do jogo
    clock.tick(snake_speed)
    # Atualiza a tela
    pygame.display.update()

# Encerra pygame
pygame.quit()
