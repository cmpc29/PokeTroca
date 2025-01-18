import random
import sqlite3
from myClient import myClient

connect = sqlite3.connect("pokedex.db")
cursor = connect.cursor()


def catch(pokemon_name): 
    chance=random.randint(1,3)
    if (chance==3):
        print("Catched!")
        return register_dex(pokemon_name)
    else:
        print(f"Oh no! {pokemon_name} runned away!")


def register_dex(pokemon_name):
    query="SELECT * FROM test WHERE species='"+pokemon_name+"';"
    cursor.execute(query)
    pokeData=cursor.fetchone()

    if (pokeData): 
        print ("Known Pokemon:\n")
        return(pokeData)

    else:
        pokemon=myClient(pokemon_name) #acessa a dex nacional e retorna o pokemon ou nao
        if (pokemon):
            insert_in_db(pokemon)
            print ("New Pokemon added!")
            cursor.execute(query)
            pokeData=cursor.fetchone()
            return(pokeData)
        else:
            print("Your captured Pokemon is not a Pokemon. RUN!")


def insert_in_db(pokemon):
    if (pokemon[3]): #2tipos
        query="INSERT INTO test (dexID,species,tipo1,tipo2,category,height,weight,description,ability) VALUES ('"
        for i,pokeData in enumerate(pokemon):
            if (i==len(pokemon)-1):
                query+=str(pokeData)
            else:
                query+=str(pokeData)+"','"
        query+="');"
        
    
    else: #1tipo
        query="INSERT INTO test (dexID,species,tipo1,category,height,weight,description,ability) VALUES ('"
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
    query="SELECT * FROM test"
    cursor.execute(query)
    pokesData=cursor.fetchall()
    print(*pokesData,sep="\n")

def check_dex(pokemon_name):
    query="SELECT * FROM test WHERE species='"+pokemon_name.title()+"';"
    cursor.execute(query)
    pokeData=cursor.fetchone()
    if (pokeData):
        print (*pokeData,sep="\n")
    else:
        print("Pokemon ainda desconhecido")