import pygame
from pygame.locals import *
from random import randint

# Global var
SCORE1 = 0
SCORE2 = 0
RIVAL = False

class Circle():

  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.vel_x = 5
    self.vel_y = 5

def main():
  #pygame setup
  pygame.init()
  screen = pygame.display.set_mode((1024, 768))
  clock = pygame.time.Clock()
  running = True
  dt = 1
  # window name
  pygame.display.set_caption("Pong")

#  print(screen.get_width() / 2)
#  print(screen.get_height() / 2)

  player1_rgb = (66, 176, 245)
  player2_rgb = (245, 66, 81)

  # game board
  rect = Rect(10 , 50, 1004, 708)

  # collision object
  collision_surface = Rect(10, 70, 1004, 668)

  # player objects
  rect_player1 = Rect(20, 354, 10, 50)
  rect_player2 = Rect(994, 354, 10, 50)

  # ball starting object
  ball = Circle(512,randint(300, 600), 10) 

  # start game
  start = False

  # random starting direction
  random_start = randint(1,4)

  # font text
  font = pygame.font.Font("freesansbold.ttf", 30)
  # main text
  text = font.render("Pong", True, (255, 255, 255), (0, 0, 0))
  text_rect = text.get_rect()
  text_rect.center = (screen.get_width() / 2, 25)
  
  # button to start game with player2
  font_button = pygame.font.Font("freesansbold.ttf", 25)
  button_surface = pygame.Surface((400, 30))
  button_text = font_button.render("Play with Rival", True, (255, 255, 255), player2_rgb)
  button_text_rect = button_text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
  # rect button
  button_rect = pygame.Rect(30, 10, 400, 30)

#  player1_rgb = (66, 176, 245)
#  player2_rgb = (245, 66, 81)

  # scoreboard text
  # score1 blue
  global SCORE1, SCORE2
  score1_text = font.render(str(SCORE1), True, (66, 176, 245), (0, 0, 0))
  score1_text_rect = score1_text.get_rect()
  score1_text_rect.center = (251, 200)
  # score1 blue
  score2_text = font.render(str(SCORE2), True, (245, 66, 81), (0, 0, 0))
  score2_text_rect = score2_text.get_rect()
  score2_text_rect.center = (751, 200)

  

  while running:
  
    # rival online or not
    global RIVAL
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      #check for mouse button event
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if button_rect.collidepoint(event.pos):
          RIVAL = True
          SCORE1 = 0
          SCORE2 = 0
          main()
          #print("button clicked!")
    
    keys = pygame.key.get_pressed() 
    # start game
    if keys[pygame.K_SPACE]:
      start = True

    # checking coordinates x, y for rect_player1, and rect_player2
    print(f"rect_player1 -> x: {rect_player1.x}", f"y: {rect_player1.y}")
    print(f"rect_player2 -> x: {rect_player2.x}", f"y: {rect_player2.y}")
    # ball movement

    if start:
    
      if random_start == 1:
      # right up
        ball.y -= ball.vel_y
        ball.x += ball.vel_x
      if random_start == 2:
      # left down
        ball.y += ball.vel_y
        ball.x -= ball.vel_x
      if random_start == 3:
      # right down
        ball.y += ball.vel_y
        ball.x += ball.vel_x
      if random_start == 4:
      # left up
        ball.y -= ball.vel_y
        ball.x -= ball.vel_x

        # bounce from wall, if player hit bounce, and keep direction
      if ball.y >= rect_player1.top and ball.y <= rect_player1.bottom and ball.x - ball.radius <= rect_player1.left and ball.x + ball.radius >= rect_player1.right:
        ball.vel_x *= -1
        player1_rgb = (255,255,255)
        print("hit")
      else:
        player1_rgb = (66, 176, 245)
      if ball.y >= rect_player2.top and ball.y <= rect_player2.bottom and ball.x - ball.radius <= rect_player2.left and ball.x + ball.radius >= rect_player2.right:
        ball.vel_x *= -1
        player2_rgb = (255,255,255)
        print("hit")
      else:
        player2_rgb = (245, 66, 81) 

       # if opposite wall hit, gain a point // TODO
      if ball.x - ball.radius < collision_surface.left:
        SCORE2 += 1
        main()
      if ball.x + ball.radius > collision_surface.right:
        SCORE1 += 1
        main()
      #if ball.x - ball.radius < collision_surface.left or ball.x + ball.radius > collision_surface.right:
        #ball.vel_x *= -1
      if ball.y - ball.radius < collision_surface.top or ball.y + ball.radius > collision_surface.bottom:
        ball.vel_y *= -1

    # move player1 
    if keys[pygame.K_w]:
      rect_player1.y -= 300 * dt
    if keys[pygame.K_s]:
      rect_player1.y += 300 * dt
    rect_player1.clamp_ip(collision_surface)
    # if clicked, create a new game with 0 - 0 scores and you can use the keys
    if RIVAL:
    # move player2 if player2 is on play with these keys
      if keys[pygame.K_i]:
        rect_player2.y -= 300 * dt
      if keys[pygame.K_k]:
        rect_player2.y += 300 * dt
    else:
      # a computer player 
      print(rect_player2.y)
      if ball.y != rect_player2.y:
        rect_player2.y = ball.y

    rect_player2.clamp_ip(collision_surface)
    

        
    # button to start game with player2
    button_surface.blit(button_text, button_text_rect) 
    screen.blit(button_surface, (button_rect.x, button_rect.y))

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

    # render text
    screen.blit(text, text_rect)
    screen.blit(score1_text, score1_text_rect)
    screen.blit(score2_text, score2_text_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

  pygame.quit()



if __name__ == "__main__":
  main()


