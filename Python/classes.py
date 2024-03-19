# __init__ será chamada toda vez que o objeto for criado

class Point() :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p = Point(2, 8)

print(p.x)        
print(p.y)       


class Flight() :
    def __init__(self, capacity):
        self.capacity = capacity 
        self.passangers = []
    
    def add_passaenger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)  
        return True  
    
    def open_seats(self):
        return self.capacity - len(self.passangers)    
        
flight = Flight(3)

people = ["Harry","Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passaenger(person):
        print(f"Adicionado {person} com sucesso ao voo")
    else:
        print(f"Não há mais assentos disponiveis para {person}")   
         
print(flight.passangers)       



        