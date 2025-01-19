import requests
import sqlite3
import random

connect = sqlite3.connect("pokedb.db")
cursor = connect.cursor()




def getPokeData(pokemon_info,pokemon_info2):
    lista_retorno=[]

    pokeID=pokemon_info.pop("dexID")
    lista_retorno.append(str(pokeID)) 

    pokeSpec=pokemon_info.pop("species")
    lista_retorno.append(pokeSpec.title()) 

    poke_T=pokemon_info.pop("types")
    lista=[]
    for _ in range(len(poke_T)):
        aux=poke_T[_]
        aux2=aux.pop("type").pop("name")
        lista.append(aux2.title())
    lista_retorno.append(lista)

    pokeDes=pokemon_info2.pop("description")[6].pop("flavor_text")
    pokeDes=pokeDes.replace("\n"," ")
    lista_retorno.append(str(pokeDes)) 

    poke_H=pokemon_info.pop("height")
    lista_retorno.append(str(poke_H/10))

    poke_W=pokemon_info.pop("weight")
    lista_retorno.append(str(poke_W/10)) 

    pokeCat=pokemon_info2.pop("category")[7].pop("genus")
    lista_retorno.append(pokeCat) 

    poke_Ab=pokemon_info.pop("abilities")
    lista=[]
    for _ in range(len(poke_Ab)):
        aux=poke_Ab[_]
        aux2=aux.pop("ability").pop("name")
        lista.append(aux2.title())
    lista_retorno.append((lista))
    return lista_retorno


def insert_in_db(pokeData):
    
    if len(pokeData[2])==2:
        query="INSERT INTO pokedex_nacional (dexID,species,tipo1,tipo2,description,height,weight,category,ability) VALUES ('"
        for i in range(len(pokeData)-1):
            if isinstance(pokeData[i],list):
                for j,k in enumerate (pokeData[i]):
                    query+=k+"','"
            else:
                query+=pokeData[i]+"','"
        query+=pokeData[-1][random.randint(0,len(pokeData[-1])-1)]+"');"
        return query
    
    else:
        query="INSERT INTO pokedex_nacional (dexID,species,tipo1,description,height,weight,category,ability) VALUES ('"
        for i in range(len(pokeData)-1):
            if isinstance(pokeData[i],list):
                for j,k in enumerate (pokeData[i]):
                    query+=k+"','"
            else:
                query+=pokeData[i]+"','"
        query+=pokeData[-1][random.randint(0,len(pokeData[-1])-1)]+"');"
        return query
    

for _ in range(152,253):
    url = f"https://pokeapi.co/api/v2/pokemon/{_}"
    response=requests.get(url)

    if response.status_code==200:
        pokemon_data=response.json()
        pokemon_info= {
            "dexID"       : pokemon_data["id"],#0
            "species"     : pokemon_data["name"],#1
            "types"       : pokemon_data["types"],#2/3
            "height"      : pokemon_data["height"],#5
            "weight"      : pokemon_data["weight"],#6
            "abilities"   : pokemon_data["abilities"]#8
        }


    url = f"https://pokeapi.co/api/v2/pokemon-species/{_}"
    response2=requests.get(url)
    if response.status_code==200:
        pokemon_data=response2.json()
        pokemon_info2= {
            "description"  : pokemon_data["flavor_text_entries"],#4
            "category"     : pokemon_data["genera"]#7
        }
        

    pokeData=getPokeData(pokemon_info,pokemon_info2)
    cursor.execute(insert_in_db(pokeData))
    connect.commit()