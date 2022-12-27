
import requests  # import module

pokemon = input("Name your Pokemon : ")   #get input
pokemon = pokemon.lower()   #lowercase input

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"    #api call
req = requests.get(url)

if req.status_code ==200:
    data = req.json()
    print("Name :",data['name'])
    print("Abilities :")
    for i in data['abilities']:
        print(i['ability']['name'],end=" ")
else:
    print("Pokemon not Found !")

