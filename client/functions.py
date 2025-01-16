import random
import sqlite3

connect = sqlite3.connect("pokedex.db")
cursor = connect.cursor()


def catch(pokemon): 
    chance=random.randint(1,3)
    if (chance==3):
        print("Catched!")
        register_dex(pokemon)
        
    else:
        print(f"Oh no! {pokemon.species} runned away!")


def register_dex(pokemon):
    if (poke_in_dex(pokemon)):
        print ("Known Pokemon.")
        query="SELECT * FROM dex WHERE species='"+pokemon.species+"';"
        cursor.execute(query)
        result=cursor.fetchone()
        print (*result[1:],sep='\n')

    else:
        "Acessar bd_online e registrar na dex local"
        print ("New Pokemon added! e dados")


def poke_in_dex(pokemon):
    query="SELECT 1 FROM dex WHERE species='"+pokemon.species+"';"
    cursor.execute(query)
    result=cursor.fetchone()
    if result:
        return True
    else:
        return False




# def check_dex(pokemon):
#     if (pokemon in "bd_local"):
#         print ("dados")
#     else:
#         print("Pokemon ainda desconhecido")
