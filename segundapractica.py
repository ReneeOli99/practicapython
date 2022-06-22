nombre = input("Introduce tu nombre: ") #Para personalizar un acceso y se ingrese el nombre de la persona
#estas son las 3 posibles formas de concatenar (unir textos)
print(f"Hola {nombre}")
print("Hola {}".format(nombre))
print("Hola "+ nombre)

edad = input("¿Cuantos años tienes? ")
edadstring = str(edad) #Convertir entero a string
booleanos = False

print(type(edad))
print(type(edadstring))

edad = int(edad) #transformas un string en un entero

#Como utilizar el if es decir hacer varias condicionantes
if edad >= 18 and edad < 100 : # si la edad es mayor o igual a 18 y menor a 100 entonces
    print("Hola"+ nombre +"eres bienvenido") 
elif edad >= 100 : # si no, entonces edad es mayor o igual a 100
    print("hola dinosaurio")
elif edad <= 0: #si no, entonces edad es menos o igual a 0
    print("No existes")
else : #si no cumple con ninguna de las reglas anteriores entonces
    print("No puedes pasar "+ nombre)