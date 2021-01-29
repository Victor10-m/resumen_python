# Ejercicio 1  
#como muntiplicar dos numeros sin el simbolo de multiplicacion SOLUION 
a = 4
b = 8 

resultado = 0 

for x in range(a):
        resultado += b
#print(resultado)   

# Ejercicio 2
#ingresar nombre y apellido e imprimilos al reves 
nombre = 'victor'
apellido = 'Monroy'

concatenacion = nombre +' '+apellido
#print (concatenacion[::-1])

# Ejercicio 3
#Definir una funcion  para encontrar el elemento menor de una lista 
lista =[1,2,3,4,5,-5]

menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor
#print('El numero menor de la lista es:', menor)

# Ejercicio 4
#escribir una funcionque indique si una persona es menor de edad
def esMayor(persona): #definimos la funcion 
        return persona.edad > 17 
class Persona:
        def __init__(self, edad):
            self.edad = edad
persona = Persona(15)
persona2 = Persona(21)
res1 = esMayor(persona)
res2 = esMayor(persona2)

#print(res1, res2)

# Ejecicio 5 
#escribir una funcion me indique si un numero es par o impar

def esPar(n):
        return n % 2 == 0;
resultado = esPar(13)
#print(resultado)

# Ejercicio 6 
#Escribir una palabra que indique cuantas vocales tiene una palabra 
palabra = 'victormanuel'
vocales = 0
for x in palabra:
        y = x.lower()
        vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
#print(vocales)

#Ejercicio 7
#Realiza una app que reciba numeros y realice la suma de ellos cuando el user escriba exit

lista = []
print('ingresa numero, para salir escribe exit')
while True:
        valor = input('ingrese valor: ')
        if valor == 'exit':
                break
        else:
                try:
                        valor = int(valor)
                        lista.append(valor)
                except:
                        print('dato incorrecto')
                        exit()
resultado = 0
for x in lista:
        resultado += x

print(resultado)
