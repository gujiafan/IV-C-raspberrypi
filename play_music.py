import pygame

def playMusic(string):
	pygame.mixer.init()
	pygame.mixer.music.load(string)
	pygame.mixer.music.play()
	