import pygame
from pygame.locals import *
from random import randint

class Circle():

  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.vel_x = 3
    self.vel_y = 3

def main():
  #pygame setup
  pygame.init()
  screen = pygame.display.set_mode((1024, 768))
  clock = pygame.time.Clock()
  running = True
  dt = 0

#  print(screen.get_width() / 2)
#  print(screen.get_height() / 2)

  player1_rgb = (66, 176, 245)
  player2_rgb = (245, 66, 81)

  # game board
  rect = Rect(10 , 50, 1004, 708)

  # collision object
  collision_surface = Rect(10, 70, 1004, 668)

  # player objects
  rect_player1 = Rect(20, 354, 10, 60)
  rect_player2 = Rect(994, 354, 10, 60)

  # ball starting object
  ball = Circle(502, 334, 10) 

  # start boolean
  start = False

  while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    keys = pygame.key.get_pressed() 
    # start game
    if keys[pygame.K_SPACE]:
      start = True

    index_y_hit = 0
    # checking coordinates x, y for rect_player1, and rect_player2
    print(f"rect_player1 -> x: {rect_player1.x}", f"y: {rect_player1.y}")
    print(f"rect_player2 -> x: {rect_player2.x}", f"y: {rect_player2.y}")
    # ball movement
    if start:
      ball.y -= ball.vel_y
      ball.x += ball.vel_x


#        collide_1 = pygame.sprite.collide_collide_(rect_player1, ball)  
#        collide_2 = pygame.sprite.collide_sprite(rect_player2, ball)
#        if collide_1 or collide_2:
#          print("hit")
#          ball.y -= ball.vel_y
#          ball.x += ball.vel_x
      # bounce from wall and keep direction
      if ball.y >= rect_player2.top and ball.y <= rect_player2.bottom and ball.x - ball.radius <= rect_player2.left and ball.x + ball.radius >= rect_player2.right:
        ball.vel_x *= -1
        player2_rgb = (255,255,255)
      else:
        player2_rgb = (245, 66, 81)
      if ball.y >= rect_player1.top and ball.y <= rect_player1.bottom and ball.x - ball.radius <= rect_player1.left and ball.x + ball.radius >= rect_player1.right:
        ball.vel_x *= -1
        player1_rgb = (255,255,255)
      else:
        player1_rgb = (66, 176, 245) 
      if ball.x - ball.radius < collision_surface.left or ball.x + ball.radius > collision_surface.right:
        ball.vel_x *= -1
      if ball.y - ball.radius < collision_surface.top or ball.y + ball.radius > collision_surface.bottom:
        ball.vel_y *= -1
    # move player1 
    if keys[pygame.K_w]:
      rect_player1.y -= 100 * dt
    if keys[pygame.K_s]:
      rect_player1.y += 100 * dt
    rect_player1.clamp_ip(collision_surface)

    # move player2
    if keys[pygame.K_i]:
      rect_player2.y -= 100 * dt
    if keys[pygame.K_k]:
      rect_player2.y += 100 * dt
    rect_player2.clamp_ip(collision_surface)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # draw ball
    pygame.draw.circle(screen, "purple", (ball.x, ball.y), ball.radius) 

    # draw the rectangle play
    pygame.draw.rect(screen, "white", pygame.Rect(rect), 2, 30)

    # draw the center line
    pygame.draw.line(screen, "white", (512, 50), (512, 755), 2)

    # player1 box object 
    pygame.draw.rect(screen, player1_rgb, rect_player1 ,1, 2)

    # player2 box object
    pygame.draw.rect(screen, player2_rgb, rect_player2 ,1, 2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

  pygame.quit()

if __name__ == "__main__":
  main()


