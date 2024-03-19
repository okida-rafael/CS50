#importação 
#assim importa só a função square - from functions import square
import functions # assim importa o modulo inteiro


for i in range(10):
    print(f"O quadrado de {i} é {functions.square(i)}")
    

print(functions.sum(2,3))    