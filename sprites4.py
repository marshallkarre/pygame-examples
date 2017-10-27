#!/usr/bin/env python

import sys, pygame, time, random, os
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

screen_size = (800,600)
FPS = 60

class Player(pygame.sprite.Sprite):
	def __init__(self, img, position, direction):
		pygame.sprite.Sprite.__init__(self)
		self.sheet = pygame.image.load(os.path.join('.', img)).convert()
		
		(self.width,self.height) = (44,51)
		(self.margin_x,self.margin_y) = (4,4)
		self.rect = pygame.Rect((self.margin_x,self.margin_y,self.width,self.height))
		self.image = pygame.Surface(self.rect.size).convert()
		self.image.blit(self.sheet, (0,0), self.rect)	

		self.rects = []
		for i in range(0,5):
			for j in range(0,3):
				x = (self.width + self.margin_x)*i + self.margin_x
				y = (self.height + self.margin_y)*j + self.margin_y
				self.rects.append((x,y,self.width,self.height))

		#self.image.set_colorkey((255,255,255))
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
		i = random.randint(0,len(self.rects)-1)
		self.image.blit(self.sheet, (0,0), self.rects[i])


def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()


	players = pygame.sprite.Group()	

	for i in range(0,random.randint(5,10)):
		(WIDTH,HEIGHT) = screen_size
		position = (x,y) = (random.randint(0,WIDTH),random.randint(0,HEIGHT))
		direction = (x_dir,y_dir) = (random.randint(-5,5),random.randint(-5,5))
		player = Player('sprites.png',position,direction)
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