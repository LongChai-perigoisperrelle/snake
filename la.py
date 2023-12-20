import pygame
import sys
import random

pygame.init()

# Paramètres du jeu
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 10

# Couleurs
WHITE = (255, 255, 255)
RED = (0, 0, 0)
GREEN = (255, 0, 0)

# Initialisation de la fenêtre du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake AI")

# Fonction principale
def main():
    clock = pygame.time.Clock()
    snake = [(WIDTH // 2, HEIGHT // 2)]
    apple = spawn_apple(snake)
    direction = (1, 0)  # Direction initiale

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Direction pour atteindre la pomme
        direction = get_direction(snake[0], apple)

        # Déplacement du serpent
        snake = move(snake, direction)

        # Gestion de la collision avec la pomme
        if snake[0] == apple:
            snake.append((0, 0))  # Ajouter un nouveau segment
            apple = spawn_apple(snake)  # Faire apparaître une nouvelle pomme

        # Gestion de la collision avec soi-même
        if len(snake) > 1 and snake[0] in snake[1:]:
            pygame.quit()
            sys.exit()

        # Gestion de la sortie de l'écran
        if not (0 <= snake[0][0] < WIDTH and 0 <= snake[0][1] < HEIGHT):
            pygame.quit()
            sys.exit()

        # Dessiner l'écran
        screen.fill(WHITE)
        draw_snake(snake)
        draw_apple(apple)
        pygame.display.flip()

        clock.tick(FPS)

# Fonction pour déterminer la direction pour atteindre la pomme
def get_direction(head, target):
    x_diff = target[0] - head[0]
    y_diff = target[1] - head[1]

    if x_diff > 0:
        return (1, 0)
    elif x_diff < 0:
        return (-1, 0)
    elif y_diff > 0:
        return (0, 1)
    elif y_diff < 0:
        return (0, -1)
    else:
        return (0, 0)

# Fonction pour déplacer le serpent
def move(snake, direction):
    x, y = snake[0]
    x += direction[0] * GRID_SIZE
    y += direction[1] * GRID_SIZE

    # Garder la longueur du serpent constante
    snake = [(x, y)] + snake[:-1]

    return snake

# Fonction pour dessiner le serpent
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Fonction pour faire apparaître une nouvelle pomme
def spawn_apple(snake):
    while True:
        apple = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                 random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
        if apple not in snake:
            return apple

# Fonction pour dessiner la pomme
def draw_apple(apple):
    pygame.draw.rect(screen, RED, (apple[0], apple[1], GRID_SIZE, GRID_SIZE))

if __name__ == "__main__":
    main()