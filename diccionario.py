#importamos librerias
from random import randrange

#diccionario palabras
def Diccionario():
	#declaramos variables
	diccy=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
	palabra=''

	#seleccionamos palabra
	palabra=diccy[randrange(0,len(diccy)-1)]

	#devolvemos la palabra
	return palabra

#creamos los guiones
def GuionesBajos(palabra):
	#declaramos las variables
	listaPalabraMost=[]

	#creamos los guiones
	for item in palabra:
		listaPalabraMost.append('_')

	return listaPalabraMost

#separamos la palabra en letras
def SepararPalabra(palabra):
	#declaramos variables
	listaPalabraAdiv=[]

	#separamos las letras
	listaPalabraAdiv=list(palabra)
	return listaPalabraAdiv