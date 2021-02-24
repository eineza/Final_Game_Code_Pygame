#Title Screen get hamby to refix before moving on to level 1.
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('Title_Screen.png')
pygame.display.set_caption("Action Guy")
running = True
while running:
  screen.fill((0, 0, 0))
  screen.blit(icon, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
pygame.display.update()
#from pygame import mixer
#Fix this soon: mixer.music.load("Title_Screen_Music.mp3")
#Fix this soon: mixer.music.play(-1)