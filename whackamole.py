import pygame
import random

#constants
GRID_SIZE = 32
NUM_COLS = 20
NUM_ROWS = 16
SQUARE_SIZE = 32






def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))



        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_image = pygame.image.load("mole.png")


        x = 0
        y = 0



        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = event.pos
                mole_pos = mole_image.get_rect(topleft=(x,y)) #last tricky bit that wasn't cooperating

                if mole_pos.collidepoint(x_pos, y_pos):
                    x = random.randrange(0, NUM_COLS - 1) * GRID_SIZE
                    y = random.randrange(0, NUM_ROWS - 1) * GRID_SIZE


            screen.fill("light green")

            for i in range(1, NUM_ROWS):
                pygame.draw.line(screen, "dark green", (0, i * SQUARE_SIZE), (640, i * SQUARE_SIZE))
            for i in range(1, NUM_COLS):
                pygame.draw.line(screen, "dark green", (i * SQUARE_SIZE, 0), (i*SQUARE_SIZE, 512))

            
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
