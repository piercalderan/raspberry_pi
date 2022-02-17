# Esempio di gioco fatto con Python e la lbreria PyGame.
# Pitone contro topo. Muovere le frecce direzionali per prendere il topo.
# 2015 Pier Calderan
# -*- coding: utf-8 -*-
import pygame, random, sys, traceback
from pygame.locals import *
def fine():
    try:
        print "Fine del gioco!"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()
def collisione(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
	else:return False
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]
direzione = 0
punteggio = 0
topo_pos = (random.randint(0, 590), random.randint(0, 590))
pygame.init()
superficie=pygame.display.set_mode((600, 600))
pygame.display.set_caption('PITONE e TOPO')
topo_img = pygame.Surface((20, 20))
topo_img.fill((0, 255, 0))
pitone_img = pygame.Surface((30, 30))
pitone_img.fill((255, 0, 0))
carattere = pygame.font.SysFont('freesansbold.ttf', 40)
velocita = pygame.time.Clock()
while True:
	velocita.tick(10)
	for e in pygame.event.get():
		if e.type == QUIT:
			sys.exit()
		elif e.type == KEYDOWN:
			if e.key == K_UP and direzione != 0:direzione = 2
			elif e.key == K_DOWN and direzione != 2:direzione = 0
			elif e.key == K_LEFT and direzione != 1:direzione = 3
			elif e.key == K_RIGHT and direzione != 3:direzione = 1
	i = len(xs)-1
	while i >= 2:
		if collisione(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):punti = carattere.render('FINE DEL GIOCO!', True, (0, 0, 0));superficie.blit(punti, (150, 200));fine()
		i-= 1
	if collisione(xs[0], topo_pos[0], ys[0], topo_pos[1], 20, 10, 20, 10):punteggio+=1;xs.append(700);ys.append(700);topo_pos=(random.randint(0,590),random.randint(0,590))
	if xs[0] < 0 or xs[0] > 560 or ys[0] < 0 or ys[0] > 560:punti = carattere.render('FINE DEL GIOCO!', True, (0, 0, 0));superficie.blit(punti, (150, 200));fine()
	i = len(xs)-1
	while i >= 1:
		xs[i] = xs[i-1];ys[i] = ys[i-1];i -= 1
	if direzione==0:ys[0] += 20
	elif direzione==1:xs[0] += 20
	elif direzione==2:ys[0] -= 20
	elif direzione==3:xs[0] -= 20	
	superficie.fill((255, 255, 255))	
	for i in range(0, len(xs)):
		superficie.blit(pitone_img, (xs[i], ys[i]))
	superficie.blit(topo_img, topo_pos)
	punti=carattere.render(str(punteggio), True, (0, 0, 0))
	superficie.blit(punti, (10, 10))
	pygame.display.update()
	
					
					
			


