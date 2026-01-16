###### Aca definiremos un archivo con todas las funciones que necesitaremos para nuestro programa
###### Definimos la clase Contacto que debera tener nombre, telefono, email y direccion.

class Contacto:
   
    def __init__(self, nombre, telefono, email, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        ##Devuelve una representación legible del contacto."""
        return f"{self.nombre} | Tel: {self.telefono} | Email: {self.email} | Dir: {self.direccion}"
    
def mostrar_contactos(agenda):
    print("\n--- LISTA COMPLETA ---")
    if not agenda:
        print("(La agenda está vacía)")
    else:
        for contacto in agenda:
            print(contacto)
