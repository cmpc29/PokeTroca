import random
import sqlite3

connect = sqlite3.connect("pokedb.db")
cursor = connect.cursor()


# def catch(pokemon): 
#     chance=random.randint(1,3)
#     if (chance==3):
#         print("Catched!")
#         register_dex(pokemon)
        
#     else:
#         print(f"Oh no! {pokemon.species} runned away!")


def take_from_db(pokemon):
    if (poke_in_db(pokemon)):
        query="SELECT * FROM dex WHERE species='"+pokemon.species+"';"
        cursor.execute(query)
        result=cursor.fetchone()
        return result

    else:
        "Este Pokemon não existe."
        print ("Este Pokemon não existe.")
        return False


def poke_in_db(pokemon):
    query="SELECT 1 FROM dex WHERE species='"+pokemon.species+"';"
    cursor.execute(query)
    result=cursor.fetchone()
    if result:
        return True
    else:
        return False