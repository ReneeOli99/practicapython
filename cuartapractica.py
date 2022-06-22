import requests
import matplotlib,pyplot as plt
import matplotlib.image as img

pokemon = input ("introduce el normbre de un pokémon: ") #el usuario introduce el nombre del pokemon
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

res= requests.get (url) #se hace la peticion a la url formada en la linea anterior

if res.status_code != 200: #si no salio bien la peticion (Status diferente a 200) se termina el programa
    print("pokemón no encontrado")
    exit()

imagen= img.imread(res.json(['sprite']['front_default']))
plt.title(res.json()['name'])

imgplot = plt.imshow(imagen)
plt.show()