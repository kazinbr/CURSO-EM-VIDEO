import pygame

pygame.init()

try:
  pygame.mixer.music.load('dsf021.mp3')
except pygame.error as error:
  print(f"Erro ao carregar o arquivo de música: {error}")
else:
  pygame.mixer.music.play()
  pygame.event.stop()