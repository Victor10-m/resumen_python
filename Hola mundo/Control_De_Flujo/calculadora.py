#ejemplo de calculadora con operacioones basicas 

primero = input('Ingresa numero_1: ') #hacemos la peticion de pedir numero
try: #debolvemosuna excepcion
    primero = float(primero) #usamos tipo de dato float para calcular con punto decimal
except: #especificamos la excepcio 
    primero = 'vic'
if primero == 'vic': #ejecutamos la condicon caso siento cerramos el programa
    print('no es un numero')
    exit()

segundo = input('ingresa numero_2: ')
try:
    segundo = float(segundo)
except:
    segundo = 'vic'
if segundo == 'vic':
    print('no es un numero')
    exit()
    
simbolo = input('ingresa simbolo de operacion: ')

if simbolo == '+':
    print('suma:', primero + segundo)
elif simbolo == '-':
    print('resta:', primero - segundo)
elif simbolo == '*':
    print('multiplicacion:', primero * segundo)
elif simbolo == '/':
    print('division:', primero / segundo)
else:
    print('el simbolo no es valido')
