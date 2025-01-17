import random
import sqlite3

connect = sqlite3.connect("pokedb.db")
cursor = connect.cursor()


def take_from_db(nome_pokemon):
    result=read_from_db(nome_pokemon)
    if not (result):
        return False
    return result

def read_from_db(nome_pokemon):
    query="SELECT * FROM pokemon_db WHERE species='"+nome_pokemon+"';"
    cursor.execute(query)
    result=cursor.fetchone()
    return (result)