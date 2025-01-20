import random
import sqlite3
from myClient import client_function

connect = sqlite3.connect("pokedex.db")
cursor = connect.cursor()


def catch(pokemon_name): 
    chance=random.randint(1,3)
    if (chance): #MODIFICAR PARA ENTREGA
        print("Catched!")
        return register_dex(pokemon_name)
    else:
        print(f"Oh no! {pokemon_name} runned away!")


def register_dex(pokemon_name):
    query="SELECT * FROM pokedex WHERE species='"+pokemon_name+"';"
    cursor.execute(query)
    pokeData=cursor.fetchone()

    if (pokeData): 
        print ("\nKnown Pokemon:")
        return(pokeData)

    else:
        pokemon=client_function(pokemon_name) #acessa a dex nacional e retorna o pokemon ou nao
        if (pokemon):
            insert_in_db(pokemon)
            print ("\nNew Pokemon added!\n")
            cursor.execute(query)
            pokeData=cursor.fetchone()
            return(pokeData)
        else:
            print("Your captured Pokemon is not a Pokemon. RUN!")


def insert_in_db(pokemon):
    if (pokemon[3]): #2tipos
        query="INSERT INTO pokedex (dexID,species,tipo1,tipo2,category,height,weight,description,ability) VALUES ('"
        for i,pokeData in enumerate(pokemon):
            if (i==len(pokemon)-1):
                query+=str(pokeData)
            else:
                query+=str(pokeData)+"','"
        query+="');"
        
    
    else: #1tipo
        query="INSERT INTO pokedex (dexID,species,tipo1,category,height,weight,description,ability) VALUES ('"
        for i,pokeData in enumerate(pokemon):
            if (pokeData):
                if (i==len(pokemon)-1):
                    query+=str(pokeData)
                else:
                    query+=str(pokeData)+"','"
        query+="');"
    cursor.execute(query)
    connect.commit()



def check_all_dex():
    query="SELECT * FROM pokedex"
    cursor.execute(query)
    pokesData=cursor.fetchall()
    print(*pokesData,sep="\n")

def check_dex(pokemon_name):
    query="SELECT * FROM pokedex WHERE species='"+pokemon_name.title()+"';"
    cursor.execute(query)
    pokeData=cursor.fetchone()
    print()
    if (pokeData):
            for i,j in enumerate(pokeData):
                match(i):
                    case 0:
                        continue
                    case 1:
                        print(f"DexID: {j}")
                    case 2:
                        print(f"Species name: {j}")
                    case 3:
                        print(f"Primary Type: {j}")
                    case 4:
                        print(f"Secondary Type: {j}")
                    case 5:
                        print(f"Category: {j}")
                    case 6:
                        print(f"Height: {j} m")
                    case 7:
                        print(f"Weight: {j} kg")
                    case 8:
                        print(f"Description: {j}")
                    case 9:
                        print(f"Ability: {j}\n")
    else:
        print("Pokemon ainda desconhecido ou inexistente.")