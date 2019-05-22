# funcion principal
def main():
	#declaramos ventana con tupla ancho alto
	ventana=pygame.display.set_mode((300,500))
	#le damos una titulo
	pygame.display.set_caption("Juego Ahorcado 2019")
	#declaramos variables
	palabraAdivinar=Diccionario() #obtenemos la palabra con la que jugaremos
	listaPalabraAdiv=SepararPalabra(palabraAdivinar)
	listaPalabraMost=GuionesBajos(listaPalabraAdiv)
	palabracorrecta=(' '.join(listaPalabraAdiv))
	guiones=(' '.join(listaPalabraMost))
	intentos=5
	letra=''
	a=0
	usadas=[]
	#definimos el tipo de letra
	letra30=pygame.font.SysFont("Arial",30)
	letra20=pygame.font.SysFont("Arial",20)
	imageTextoPresente=letra30.render(guiones,True,(200,200,200),(0,0,0))
	rectanguloTextoPresente=imageTextoPresente.get_rect()
	rectanguloTextoPresente.centerx=ventana.get_rect().centerx
	rectanguloTextoPresente.centery=320
	imageTextoFallos=letra30.render(str(intentos),True,(200,200,200),(0,0,0))
	rectanguloTextoFallos=imageTextoFallos.get_rect()
	rectanguloTextoFallos.centerx=ventana.get_rect().centerx
	rectanguloTextoFallos.centery=420

	#bucle principal del juego
	while True:
		#cargamos imagenes y texto
		ventana.blit(imageTextoPresente,rectanguloTextoPresente)
		ventana.blit(imageTextoFallos,rectanguloTextoFallos)
		pygame.display.flip()
		#bucle comprueba eventos
		for evento in pygame.event.get():
			#comprovamos evento para salir
			if evento.type==QUIT:
				#detiene modulos y ventana
				pygame.quit()
				sys.exit()
			elif evento.type==pygame.KEYDOWN:
				if evento.key==K_ESCAPE:
					#detiene modulos y ventana
					pygame.quit()
					sys.exit()
				elif evento.unicode.lower() in ("abcdefghijklmnopqrstuvwxyz"):
					if evento.unicode in listaPalabraAdiv and evento.unicode not in usadas:
						letra=evento.unicode
						print (letra)
						for key,value in enumerate(listaPalabraAdiv):
							if value==letra:
								listaPalabraMost[key]=value
								usadas.append(letra)
								guiones=(' '.join(listaPalabraMost))
								imageTextoPresente=letra30.render(guiones,True,(200,200,200),(0,0,0))
								ventana.blit(imageTextoPresente,rectanguloTextoPresente)
								pygame.display.flip()
					else:
						if evento.unicode not in usadas:
							letra=evento.unicode
							usadas.append(letra)
							fallo=True
							intentos=intentos-1
							imageTextoFallos=letra30.render(str(intentos),True,(200,200,200),(0,0,0))
							ventana.blit(imageTextoFallos,rectanguloTextoFallos)
							pygame.display.flip()

			#comprobamos si la partida ha acabado
			if intentos<=0:
				imageTextoFinal=letra20.render('Has fallado, la palabra era: ',True,(200,200,200),(0,0,0))
				rectanguloTextoFinal=imageTextoFinal.get_rect()
				rectanguloTextoFinal.centerx=ventana.get_rect().centerx
				rectanguloTextoFinal.centery=30
				guiones=(' '.join(listaPalabraAdiv))
				imageTextoPresente=letra30.render(guiones,True,(200,200,200),(0,0,0))
				ventana.blit(imageTextoPresente,rectanguloTextoPresente)
				ventana.blit(imageTextoFinal,rectanguloTextoFinal)
			elif listaPalabraAdiv==listaPalabraMost:
				imageTextoFinal=letra20.render("Has acertado, la palabra era ",True,(200,200,200),(0,0,0))
				rectanguloTextoFinal=imageTextoFinal.get_rect()
				rectanguloTextoFinal.centerx=ventana.get_rect().centerx
				rectanguloTextoFinal.centery=30
				guiones=(' '.join(listaPalabraAdiv))
				imageTextoPresente=letra30.render(guiones,True,(200,200,200),(0,0,0))
				ventana.blit(imageTextoPresente,rectanguloTextoPresente)
				ventana.blit(imageTextoFinal,rectanguloTextoFinal)

		#actualiza la ventana
		pygame.display.update()

if __name__=='__main__':
	import pygame
	from pygame.locals import *
	import sys
	from diccionario import *
	pygame.init()
	main()