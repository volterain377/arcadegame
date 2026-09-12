import pygame
import random

pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Tangkap Kotak")

# Warna
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Pemain
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Target
target_size = 30
target_x = random.randint(0, WIDTH - target_size)
target_y = random.randint(0, HEIGHT - target_size)

# Skor
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Batasi pemain agar tidak keluar layar
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # Rect untuk collision
    player_rect = pygame.Rect(
        player_x, player_y, player_size, player_size
    )

    target_rect = pygame.Rect(
        target_x, target_y, target_size, target_size
    )

    # Jika target tertangkap
    if player_rect.colliderect(target_rect):
        score += 1
        target_x = random.randint(0, WIDTH - target_size)
        target_y = random.randint(0, HEIGHT - target_size)

    # Gambar background
    screen.fill(WHITE)

    # Gambar pemain
    pygame.draw.rect(
        screen, BLUE,
        (player_x, player_y, player_size, player_size)
    )

    # Gambar target
    pygame.draw.rect(
        screen, RED,
        (target_x, target_y, target_size, target_size)
    )

    # Tampilkan skor
    score_text = font.render(f"Skor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update layar
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
