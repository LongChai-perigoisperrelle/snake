import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
RED = (0, 0, 0)
GREEN = (255, 0, 0)

# Paramètres du jeu
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10

# Définition des directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Fonction pour afficher le score
def draw_score(score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Fonction principale du jeu
def game():
    while True:
        snake = [(100, 100), (90, 100), (80, 100)]
        direction = RIGHT
        apple = generate_apple(snake)

        score = 0

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and direction != RIGHT:
                        direction = LEFT
                    elif event.key == pygame.K_RIGHT and direction != LEFT:
                        direction = RIGHT
                    elif event.key == pygame.K_UP and direction != DOWN:
                        direction = UP
                    elif event.key == pygame.K_DOWN and direction != UP:
                        direction = DOWN

            # Mettre à jour la position du serpent
            head = (snake[0][0] + direction[0] * CELL_SIZE, snake[0][1] + direction[1] * CELL_SIZE)
            snake.insert(0, head)

            # Vérifier si le serpent a mangé la pomme
            if head == apple:
                score += 1
                apple = generate_apple(snake)
            else:
                snake.pop()

            # Vérifier si le serpent s'est mordu la queue
            if len(snake) != len(set(snake)):
                break

            # Vérifier si le serpent a atteint les bords de l'écran
            if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
                break

            # Dessiner l'arrière-plan
            screen.fill(RED)

            # Dessiner le serpent
            for segment in snake:
                pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

            # Dessiner la pomme
            pygame.draw.rect(screen, WHITE, pygame.Rect(apple[0], apple[1], CELL_SIZE, CELL_SIZE))

            # Dessiner le score
            draw_score(score)

            pygame.display.flip()
            clock.tick(FPS)

        # Afficher l'écran de fin de jeu
        game_over(score)

# Fonction pour générer une nouvelle pomme
def generate_apple(snake):
    while True:
        apple = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if apple not in snake:
            return apple

# Fonction pour afficher l'écran de fin de jeu
def game_over(score):
    font = pygame.font.Font(None, 72)
    game_over_text = font.render(f"Game Over - Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2 - 50))

    pygame.display.flip()
    pygame.time.delay(2000)  # Pause de 2 secondes

# Lancer le jeu
while True:
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game()