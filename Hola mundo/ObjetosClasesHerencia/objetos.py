#las clases son como el plano d elos que quereqmos crear 
class Usuario:
    nombre = 'Felipe'
    apellido = 'feliz'
usuario = Usuario()
print( usuario.nombre, usuario.apellido)

#ejemplo 2 

class Usuarios:
    def __init__(self, nombre, apellido):  #el methodo init simpre se ejecuta siempre cuando hacemos instancia de las clases 
        self.nombre = nombre # palabra reservada self que hace referencia a una instancia  de esta namera entramos a la istancia
        self.apellido = apellido
usuario1 = Usuarios('Felipe', 'Feliz')
usuario2 = Usuarios('carlos', 'feliz')
print(" Datos de usuario 1:",usuario1.nombre, usuario1.apellido,"\n","Datos de usuario 2:", usuario2.nombre, usuario2.apellido)

#ejemplo 3 Metodos
#Metodo es una funcio que pertenece a un objeto
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre   = nombre
        self.apellido = apellido
    def saludar(self):
        print('hola, mi nombre es:', self.nombre, self.apellido)

usuario1 = Persona('Felipe', 'Feliz')
usuario2 = Persona('carlos', 'feliz')

usuario1.saludar() 
usuario1.nombre = 'chanchito' #para poder cambiar el nombre de nuestra instancia de esta manera 
usuario1.saludar() #volvemos a llamar elmetodo pero con las modificaciones actuales 
usuario2.saludar()