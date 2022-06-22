from multiprocessing.spawn import import_main_path
import random #libreria para generar datos aleatorios

#Libreria para generar graficas
#Para instalar esto necesita copiar, pegar y ejecutar tu terminal
import matplotlib.pyplot as plt

print(random.randrange(10,100,2)) #generar un numero aleatorio y lo imprime

lista = [1, 2, 3, 4, 5, 6, 7, 8,9, 10] #Declarar una lista
print('Lista original', lista) #imprime la lista

random.shuffle(lista)#mezcla elementos de la lista al azar
print('Lista mixeada', lista) #imprime la lista mezclada


campana = [random.gauss(1, 0, 5) for i in range(1000)] #genera una grafica de campana de gauss y genera los datos de la grafica
print(campana)

plt.hist(campana, bin=15) #arma la grafica
plt.show() #muestra la grafica