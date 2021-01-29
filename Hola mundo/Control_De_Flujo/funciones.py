#las funcioones su principal funcion es que reciben argumentos los argumentos son variables
def Funcion1():
    print('mi primera funcion')
Funcion1()

#tic dentro de las funciones van los argumentos(variables) despues de print
# la funcion la llamamos y escribimos los valores de las variables 
def ImprimeDato(Nombre, Apelido):
    print('El nombre completo es: ' , Nombre, Apelido )
ImprimeDato('Victor', 'Monroy')

#para asar mas de un argumento a muestro agrumento usamos el simbnolo reservado *
def ImprimeDatoDos(*nombre):
    print ('resultado: ', nombre)
ImprimeDatoDos('Victor', 'Manuel', 'Monroy')

#para asar mas de un argumento a muestro agrumento usamos el simbnolo reservado *
def ImprimeDatoDos(*nombre):
    print ('resultado: ', nombre[0]) #[0] especificamos entrar a la posicion de la tupla ACCEDEMOS A LOS VALORES DEL ARGUMENTO
ImprimeDatoDos('Victor', 'Manuel', 'Monroy')

#OTRA FORMA PARA ACCEDER A las variables de nuestroa argumento es de la siguente manera sin importar la posicion en el argumento
def ImprimeDatoTres(Apellido, Nombre ):
    print(Nombre, Apellido)
ImprimeDatoTres(Nombre='victor', Apellido='Manuel')

#otra manera de acceder a los agrmuentos primeros los agrupamos como si fuern diccionario y accedo a las llaves del diccionario usando las sintaxis de diccioinario
#esta manera se me hace mas facil
def ImprimeDatoCuatro(**kwargs):
    print(kwargs['Nombre'], kwargs['Apellido'])
ImprimeDatoTres(Nombre='victor', Apellido='Manuel')


def MiFuncion(argumeto = 'chanchito'):
    print(argumeto)
MiFuncion('batman')
MiFuncion()

#ejemplo de funcion con lista la lista de define dentro de la funcion
def Mifuncionlista(lista):
    for el in lista:
        print(el)
Mifuncionlista(['hola: ', 'chanchito', 'feliz'])

#funcion de ejemplo para concatenas valores de una slista de nombres
def Nombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return(i)
nombres = Nombres(["Nombres: ", 'victor', 'Manuel'])

print(nombres)