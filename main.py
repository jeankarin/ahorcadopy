def main():
	#declaramos ventana con tupla ancho alto
	ventana=pygame.display.set_mode((300,500))
	#le damos una titulo
	pygame.display.set_caption("Juego Ahorcado 2019")

	#bucle principal del juego
	while True:
		#bucle comprueba eventos
		for evento in pygame.event.get():
			#comprovamos evento para salir
			if evento.type==QUIT:
				#detiene modulos y ventana
				pygame.quit()
				sys.exit()
		#actualiza la ventana
		pygame.display.update()

if __name__=='__main__':
	import pygame
	from pygame.locals import *
	import sys
	pygame.init()
	main()