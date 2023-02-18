import pygame
import time
import random

pygame.init()

screensize = (200,200) # This is a Vector 2 Dimentional Object

screen = pygame.display.set_mode(screensize)

run = True

color = (250, 153, 0)

displacement = 0
x_pos = 200
x_pos_2 = 300
y_pos = 95

pipeno = 0
pipeno2 = 0

gamepipes = 10

loclist = []
for a in range(gamepipes):
	loclist.append(random.randint(-20,40))

loclist2 = []
for b in range(gamepipes):
	loclist2.append(random.randint(-20,40))

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	screen.fill(color)

	pygame.draw.rect(screen, (255,255,255), pygame.Rect(95, y_pos, 20, 20))
	
	pygame.draw.rect(screen, (255,255,255), pygame.Rect(x_pos, loclist[pipeno], 20, 60))
	pygame.draw.rect(screen, (255,255,255), pygame.Rect(x_pos, 120 + loclist[pipeno], 20, 60))

	pygame.draw.rect(screen, (255,255,255), pygame.Rect(x_pos_2, loclist2[pipeno2], 20, 60))
	pygame.draw.rect(screen, (255,255,255), pygame.Rect(x_pos_2, 120 + loclist2[pipeno2], 20, 60))
	
	displacement = 3
	x_pos -= displacement
	x_pos_2 -= displacement

	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		y_pos -= 8
	
	y_pos += 2

	if x_pos <= 0:
		x_pos = 200
		pipeno += 1
	if x_pos_2 <= 0:
		x_pos_2 = 200
		pipeno2 += 1

	if y_pos >= 200:
		run = False
		print("game over!")

	rect1 = pygame.Rect(95, y_pos, 20, 20)
	rect2 = pygame.Rect(x_pos, loclist[pipeno], 20, 60)
	rect3 = pygame.Rect(x_pos, 120 + loclist[pipeno], 20, 60)
	rect4 = pygame.Rect(x_pos_2, loclist2[pipeno2], 20, 60)
	rect5 = pygame.Rect(x_pos_2, 120 + loclist2[pipeno2], 20, 60)

	collideTest1 = rect1.colliderect(rect2)
	collideTest2 = rect1.colliderect(rect3)
	collideTest3 = rect1.colliderect(rect4)
	collideTest4 = rect1.colliderect(rect5)

	if collideTest1 == 1 or collideTest2 == 1 or collideTest3 == 1 or collideTest4 == 1:
		print("game over")
		run = False

	time.sleep(0.033)
	pygame.display.update()

print(f"Total Pipes: {pipeno + pipeno2}")
