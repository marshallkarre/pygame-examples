#!/usr/bin/env python

import sys, pygame, time, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

screen_size = (800,600)
FPS = 60

class Player(pygame.sprite.Sprite):
	def __init__(self, color, position, direction):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		(x,y) = position
		self.rect.x = x
		self.rect.y = y
		self.direction = direction

	def update(self):
		(x,y) = self.direction
		self.rect.x += x
		self.rect.y += y
		(WIDTH,HEIGHT) = screen_size
		if self.rect.left > WIDTH:
			self.rect.right = 0
		if self.rect.right < 0:
			self.rect.left = WIDTH
		if self.rect.top > HEIGHT:
			self.rect.bottom = 0
		if self.rect.bottom < 0:
			self.rect.top = HEIGHT



def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()

	colors = [(134,142,150),(250,82,82),(230,73,128),(190,75,219),(121,80,242),(76,110,245),(34,138,230),(21,170,191),(18,184,134),(64,192,87),(130,201,30),(250,176,5),(253,126,20),(233,236,239),(255,236,153),(163,218,255)]	

	players = pygame.sprite.Group()	

	for i in range(0,random.randint(5,10)):
		(WIDTH,HEIGHT) = screen_size
		position = (x,y) = (random.randint(0,WIDTH),random.randint(0,HEIGHT))
		color = colors[random.randint(0,len(colors)-1)]
		direction = (x_dir,y_dir) = (random.randint(-5,5),random.randint(-5,5))
		player = Player(color,position,direction)
		players.add(player)

	while True:
		clock.tick(FPS)
		screen.fill((0,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEMOTION:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()

		players.update()
		players.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
	main()