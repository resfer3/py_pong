import pygame
from pygame.locals import *

def main():
  #pygame setup
  pygame.init()
  screen = pygame.display.set_mode((1024, 768))
  clock = pygame.time.Clock()
  running = True
  dt = 0

  #player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

  print(screen.get_width() / 2)
  print(screen.get_height() / 2)

  # 1004
  rect = Rect(10 , 50, 1004, 708)

  while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")


    # draw the rectangle play
    pygame.draw.rect(screen, "white", pygame.Rect(rect), 2, 30)

    # draw the center line
    pygame.draw.line(screen, "white", (512, 50), (512, 755), 2)


  #  keys = pygame.key.get_pressed()
  #  if keys[pygame.K_w]:
  #    player_pos.y -= 300 * dt
  #  if keys[pygame.K_s]:
  #    player_pos.y += 300 * dt
  #  if keys[pygame.K_a]:
  #    player_pos.x -= 300 * dt
  #  if keys[pygame.K_d]:
  #    player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

  pygame.quit()

if __name__ == "__main__":
  main()


