class Pokemon:
    def __init__(self,species,type1=None,type2=None,description=None,height=None,weight=None,category=None,ability=None):
        self.species=species
        self.type1=type1
        self.type2=type2
        self.description=description
        self.height=height
        self.weight=weight
        self.category=category
        self.ability=ability

name=input().upper()
name=name[0].upper()+name[1:].lower()
x=Pokemon(name)
x=False

if x:
    print(x.species)
else:
    print("falso")
