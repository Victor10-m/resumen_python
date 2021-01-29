#clase pricipal la cual a a heredar datos a las clases gato y perro
class Animal:
    def __init__(self, nombre, sonido): #con el metodo init inicializamos los atributos de las clases 
        self.nombre = nombre
        self.sonido = sonido
    
    def saludar(self):
        print('hola, soy un', self.tipo, ' y mi sonido es', self.sonido)
#calse gato        
class Gato(Animal):
    tipo = 'gato'
    #forma de extender el metodo init del padre 
    def __init__(self, nombre, sonido):
        Animal.__init__(nombre, sonido)
        print('gato extendido')

#clase perro
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
    print('perro extendido')

#clase vaca
class Vaca (Animal):
    tipo = 'vaca'

gato = Gato('lino', 'maullido')
gato.saludar() #llamamos al metodo saluodar
perro = Perro('yunko', 'ladrido')
perro.saludar() #llamamos al metodo saluodar
vaca = Vaca('vaquita', 'muuu')
vaca.saludar()