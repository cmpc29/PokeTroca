import sqlite3

connect = sqlite3.connect("pokedb.db")
cursor = connect.cursor()


def take_from_db(nome_pokemon):
    result=read_from_db(nome_pokemon)
    if (result):
        return result
    return False

def read_from_db(nome_pokemon):
  
    query="SELECT * FROM test WHERE species= '"+nome_pokemon+"';"
    cursor.execute(query)
    result=cursor.fetchone()
    return (result)
