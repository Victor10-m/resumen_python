#usaremos append para agregar un nombre o numero mas al final de la lista 
#lista para letas 
lista = ["Lista1", "Lista2", "lista3"]
#para hacer la coìa de la una variable basta con usar el methodoc copy 
copiaVariableLista = lista.copy()
lista.append("lista4")

#lsiat de numeros 
listaNumero = [1,2,3,3]
listaNumero.append(4)

#para mandar a lipiar la variable lista usaremos el metodo clear
#lista.clear()

#el metodo Count estemetodo nos permite contar el numero de veces que se repite algun valor en este caso el valor de 3
print(lista, '\n',copiaVariableLista, '\n', listaNumero.count(3))

#para saber cuentos elementos tiene una lista usamos el metodo len
print( len(lista ))

#elementos de una lista 
# Usando el [] y dentro de ellos escribimos la posicion de la lista que deseamos imprimir en swte caso la 1
folio1 = 'maria', 'juan'

print ( folio1 [0])

#Eliminar elementos de la lista 
lista.pop() #este metodo nos permite eliminar solamnete el ultimo elemmento de la lista 
coleccion = ['autos', 'motos']
coleccion.remove('autos') #metodo para eliminar un elemento especificode la coleccion 

print( coleccion )

#reverse  y sorf 
variable = ['uno', 'dos', 'tres']
#variable.reverse() #metodo que nos ordena de manera contraria el contenido de la variable 
variable.sort() #metodo que recorre un posision en el arreglo

print(variable)