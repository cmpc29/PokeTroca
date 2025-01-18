from functions import catch


while True:
    pokemon_name=input().title()
    pokeData=catch(pokemon_name)
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
                    print(f"Ability: {j}")
