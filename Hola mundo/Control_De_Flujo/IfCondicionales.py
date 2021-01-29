# condicional if

# a == b nos hace referncia para igualar una variable es igual a otra 
# a < b monor que
# a > b mayor que
# a != b diferente
# a <= b menos o igual 
# a >= b mayor o igual 
#if 2 > 5
    #print('2 es menor que 5')

if 2 > 5:
    print('dos en menor que cinco en if')
elif 2 > 5:  #elif es un condicionante que evalua a if estasolo se ejecuta cundo if es falso
    print('2 es menor que 5 en enif')
else:
    print('si las condiciones anteriores no se cumplen me ejecuto yo')

#if ternario se ledenomina asi por que evalua dodnformas ya sea falso  verdadero
print('Cuando debuenlve true') if 5 > 2 else print('Cuando debuelve false')

# condicional AND
#para hacer uso del sondicional and (Y) ambas deben de ser true de lo contrario el false no se imprime
if 2 < 5 and 3 > 2:
    print ('usando "and" las 2 condiciones deberas de ser true')
if 2 > 5 and 3 > 2: #esta instruccon no se ejecuta por que una de la scondicines no se cumpe
    print ('usando "and" las 2 condiciones deberas de ser true caso contrio no se imprime')

# condicional OR (o) esta se ejeucuta cuando aunque sea 1 sea verdadero 
if 5 < 0 or 5 > 0:
    print('Esta se ejecuta cuando el codigo sea las 2 verdaderos Ò incluso habiendo una falsa')
if 5 < 0 or 10 < 5: #instruccion que no se ejecuta ya que las conciiones son falsas 
    print('cuando ambas esta en false no se ejecuta')