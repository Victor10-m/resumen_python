#ŧuplas una vez creada n se puede modifiucar para cambiarla nesesariamente deveras crear una copia y incluir datos ...
tupla = ('Hola ', 'mi nombre es: ', 'Victor ' 'Manuel ' 'Monroy ' 'Angeles')

#print(tupla.index('Hola')) # ste metodo 

#rango 
rango = range(5)
print(rango)

#diccionaros en python 
Diccionarios = {
    "Nombre"   : "Victor Manuel",
    "Apellido" : "Monroy Angeles",
    "Edad"     : 22 
}
print(Diccionarios) #de esta manera imprimimos todos los datos del dicc... 
print(Diccionarios['Nombre'])  # de esta manera imprimimos in dato en especifico del dicccionario
print(Diccionarios.get('Nombre')) #usando el metodo get igual podemos aceder a un dato del diccionario

#para cambiar el valor dentro del diccionario lo que debemos de hacer es lo sigueinte 
Diccionarios['Nombre'] = 'Manuel Victor'

Diccionarios['Estado'] = 'Hidalgo' #esta forma nos permite agregar un nuevo valor a nuestro diccionario
print(Diccionarios)

Diccionarios.pop('Estado') #usandoe l metodo pop podemos  eliminar propiedades de nuestro diccionario
print(Diccionarios)

Diccionarios.popitem() #este metodo nos permite eliminar el untimo dato de nuesto diccionario
print(Diccionarios)

del Diccionarios['Apellido'] #este metodo de igual manera nos permit eliminar el ultimo valor del diccionario
print(Diccionarios)

clone = Diccionarios.copy() #Este metodo nospermite crear un copia de las variables siognada en variable nueva 
print(Diccionarios, clone)

clone2 = dict(Diccionarios) #este metodo nos permite de igua manera haer una copia de uan variable
print (clone2)