import pygame

pygame.init()
screen_info = pygame.display.Info()
print (screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)

fish_image = pygame.image.load('fish.png')
fish_image = pygame.transform.smoothscale(fish_image, (80, 80))
fish_rect = fish_image.get_rect()
fish_rect.center = (400, 300)

speed = pygame.math.Vector2(0,10)

def move_fish():
  global fish_image
  screen_info = pygame.display.Info()
  fish_rect.move_ip(speed)
  if fish_rect.bottom > screen_info.current_h:
    speed[1] *= -1
    fish_image = pygame.transform.flip(fish_image, False, True)
    fish_rect.move_ip(0, speed[1])

def main():
  while True:
    clock.tick(60)
    move_fish()
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()

if __name__=='__main__':
  main()
