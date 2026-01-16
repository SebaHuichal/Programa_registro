
### Aca definimos la cuarta funcion de nuestro programa.
### Definiremos la opcion 4 (en nuestro main).

def eliminar_contacto(agenda):
    
    print("\n--- ELIMINAR CONTACTO ---")
    nombre_buscar = input("Ingrese el nombre del contacto a eliminar: ")
    
    for i, contacto in enumerate(agenda):
        if contacto.nombre.lower() == nombre_buscar.lower():
            confirmacion = input(f"¿Está seguro de eliminar a {contacto.nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                agenda.pop(i) # Elimina el elemento en la posición i
                print(" Contacto eliminado.")
            else:
                print("Operación cancelada.")
            return

    print(" No se encontró el contacto.")
    
def mostrar_contactos(agenda):
    """
    Muestra todos los contactos guardados en la agenda.
    """
    print("\n--- LISTA COMPLETA ---")
    if not agenda:
        print("(La agenda está vacía)")
    else:
        for contacto in agenda:
            # Al hacer print(contacto), Python usa automáticamente el __str__ de la Clase
            print(contacto)