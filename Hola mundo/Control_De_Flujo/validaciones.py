#ema de validacion de condicion y caso contrio usamos funcion exit para finalizar el proceso
Nombre = input('ingresar tu nombre: ')
try:
    Nombre = str(Nombre)
except:
    Nombre = '10'
if Nombre == '10':
    print('no es string')
    exit()

primero = input('Ingresa numero_1: ')
try:
    primero = int(primero)
except:
    primero = 'vic'
if primero == 'vic':
    print('no es un numero')
    exit()

segundo = input('ingresa numero_2: ')
try:
    segundo = int(segundo)
except:
    segundo = 'vic'
if segundo == 'vic':
    print('no es un numero')
    exit()
    
print("\n","Su nombre es: ", Nombre,"\n","Resutado de suma de numeros", primero + segundo )