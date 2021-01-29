#ejemplo de herencia 
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):
        print('hola, mi nombre es: ', self.nombre, self.apellido)
class Admin(Usuario):
    def SuperSaludo(self):
        print('hola!, Mi nombre es: ', self.nombre, 'y soy administrador ')
Usuario = Usuario('victor', 'manuel')
Usuario.saludo()
Usuario.nombre = 'cristi'
Usuario.saludo()

admin = Admin('Manuel', 'Feliz')
admin.saludo()
admin.SuperSaludo()