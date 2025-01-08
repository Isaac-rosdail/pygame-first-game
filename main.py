import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
fps = 30

# Snake setup
player = pygame.Rect((300, 250, 25, 25))
movement = "RIGHT"

# Game loop

run = True
while run:

    # Fill screen with black each frame to "clear" rectangles
    screen.fill((0, 0, 0))

    # Draw player rectangle
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Event handlers for quitting / movement / etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movement = "LEFT"
            if event.key == pygame.K_d:
                movement = "RIGHT"
            if event.key == pygame.K_w:
                movement = "UP"
            if event.key == pygame.K_s:
                movement = "DOWN"

    # Update position based on movement value
    match movement:
        case "LEFT":
            player.move_ip(-5, 0)
        case "RIGHT":
            player.move_ip(5, 0)
        case "UP":
            player.move_ip(0, -5)
        case "DOWN":
            player.move_ip(0, 5)

    # Update diaplay to draw elements
    pygame.display.update()
    clock.tick(fps)

pygame.quit()