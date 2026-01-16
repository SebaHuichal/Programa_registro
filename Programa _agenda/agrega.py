from datos import Contacto

### Aca definimos la primera funcion de nuestro programa.
### Definiremos la opcion 1 (en nuestro main).

def agregar_contacto(agenda):
    print("\n--- REGISTRAR CONTACTO ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Correo: ")
    direccion = input("Dirección: ")

    # Creamos el objeto Contacto
    nuevo_contacto = Contacto(nombre, telefono, email, direccion)
    
    # Lo guardamos en la lista (Estructura de datos: Lista) 

    agenda.append(nuevo_contacto)
    print(" Contacto registrado exitosamente.")