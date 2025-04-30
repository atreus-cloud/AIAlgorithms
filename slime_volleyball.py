import pygame
import random
from minimax_alpha_beta import MinimaxAI, AlphaBetaAI

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SLIME_WIDTH = 50
SLIME_HEIGHT = 50
BALL_SIZE = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slime Volleyball")

# Define Slime class
class Slime(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((SLIME_WIDTH, SLIME_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    
    def update(self, move_direction):
        if move_direction == "left":
            self.rect.x -= self.speed
        elif move_direction == "right":
            self.rect.x += self.speed
        # Prevent slimes from going out of bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - SLIME_WIDTH:
            self.rect.x = SCREEN_WIDTH - SLIME_WIDTH

# Define Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.x_speed = 5
        self.y_speed = 5
    
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ball bouncing off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.y_speed *= -1

        # Ball out of bounds (left or right side)
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH // 2
            self.rect.y = SCREEN_HEIGHT // 2
            self.x_speed *= -1
            self.y_speed *= -1

# Game state functions
def game_over(state):
    ball_x, ball_y = state["ball_pos"]
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
        return True
    return False

def generate_children(state, maximizing_player):
    children = []
    possible_moves = ["left", "right"]
    for move in possible_moves:
        new_state = state.copy()
        new_state["slime1_pos"] = (state["slime1_pos"][0] - 5 if move == "left" else state["slime1_pos"][0] + 5, state["slime1_pos"][1])
        new_state["ball_pos"] = (state["ball_pos"][0] + 5, state["ball_pos"][1])
        children.append(new_state)
    return children

# Game Loop
def main():
    slime1 = Slime(100, SCREEN_HEIGHT // 2, BLUE)
    slime2 = Slime(SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2, RED)
    ball = Ball()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(slime1, slime2, ball)

    clock = pygame.time.Clock()

    # Create AI players
    minimax_ai = MinimaxAI(depth=3)
    alpha_beta_ai = AlphaBetaAI(depth=3)

    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Minimax/AlphaBeta AI movement for slime1
        minimax_move = minimax_ai.get_move(slime1, ball)
        alpha_beta_move = alpha_beta_ai.get_move(slime2, ball)

        slime1.update(minimax_move)
        slime2.update(alpha_beta_move)

        # Update ball position
        ball.update()

        # Draw all sprites
        all_sprites.draw(screen)

        # Check for game over
        if game_over({"ball_pos": (ball.rect.x, ball.rect.y)}):
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
