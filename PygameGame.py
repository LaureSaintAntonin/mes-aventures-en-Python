import pygame

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.clock = pygame.time.Clock()
		self.player = Player(0, 0)
		self.area = pygame.Rect(200, 100, 200, 200)
		self.area_color = "blue"


	def handling_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.player.velocity[0] = -1
		elif keys[pygame.K_RIGHT]:
			self.player.velocity[0] = 1
		else:
			self.player.velocity[0] = 0

		if keys[pygame.K_UP]:
			self.player.velocity[1] = -1
		elif keys[pygame.K_DOWN]:
			self.player.velocity[1] = 1
		else:
			self.player.velocity[1] = 0

	def update(self):
		self.player.move()
		if self.area.colliderect(self.player.rect):
			self.area_color = "turquoise"
		else:
			self.area_color = "blue"

	def display(self):
		self.screen.fill("black")
		pygame.draw.rect(self.screen, self.area_color, self.area)
		self.player.draw(screen)
		pygame.display.flip()

	def run(self):
		while self.running:
			self.handling_event()
			self.update()
			self.display()
			self.clock.tick(60)

class Player:
	def __init__(self, x, y):
		self.image = pygame.image.load("Leia.png")
		self.rect = self.image.get_rect(x=x, y=y)
		self.speed = 5
		self.velocity = [0, 0]

	def move(self):
		self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

	def draw(self, screen):
		screen.blit(self.image, self.rect)



pygame.init()
screen = pygame.display.set_mode((1080, 720))
game = Game(screen)
game.run()

pygame.quit()
