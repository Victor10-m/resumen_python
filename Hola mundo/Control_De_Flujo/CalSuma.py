Numero1 = input('Ingresa numero 1: ')
Numero2 = input('Ingresa numero 2: ')
N1 = int(Numero1)
N2 = int(Numero2)
print(N1 + N2)
#ejeplo ce conversion de datop string a entero 

Numero1 = input('Ingresa numero 1: ')
try:
    Numero1 = int(Numero1)
except:
    Numero1 = 'Victor' 

Numero2 = input('Ingresa numero 2: ')
try:
    Numero2 = int(Numero2)
except:
    Numero2 = 'Victor' 
if Numero1 == 'Victor' or Numero2 == 'victor':
    print('Dato incorrecto, intenta nuevamente')
else:
    print(Numero1 + Numero2)

#validaciones 

if Numero1 == 'vitor':
    print('no es un numero entero')
    exit();