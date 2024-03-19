import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Entrada invalida")    
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: não pode ser dividido por 0") 
    sys.exit(1)

print(f"{x}/{y} é igual a {result}")