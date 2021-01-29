# i = 0

# while i < 5:
#     print(i)
#     if i == 3:
#         break #breack nos permite para el programa cundo la condicion se cumple
#     i += i

# i = 0

# while i < 5:
#     i += i
#     if i == 3:
#         continue 
#     print(i)

# for loop

#usuarios = ['Juan','Carlos','Maria','Tomas']  #imprimir una lista 

#for usuario in usuarios:
#    print(usuario)

#usuariosDos = 'victor' #imprimir un string

# for c in usuariosDos:
#     print(c)

personas = ['Juan','Carlos','Maria','Tomas']

for persona in personas:
    if persona == 'Maria':
        break
    #print(persona)

personas = ['Juan','Carlos','Maria','Tomas']

for persona in personas:
    if persona == 'Maria':
        continue         #nos saltamos la posision del if
    print(persona)

#ideracion con for
#posicion 1 el numero del cual va a iniciar 
#posicion dos el valor en el que termina
#posicion tres de cuento en a imprimir el rango 
for X in range(2, 30, 3):
    print(X)
else: 
    print('Hemos terminado')

#iteracion con dos variavles un for dentro de otr for
trabajadores = ['carlos', 'daniel', 'joaquin']
salario = [1500, 1600, 1700]

for trabajador in trabajadores:
    for pago in salario:
        print(trabajador, pago)