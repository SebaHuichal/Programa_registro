
### Aca definimos la tercera funcion de nuestro programa.
### Definiremos la opcion 3 (en nuestro main).
        
def editar_contacto(agenda):
    
    print("\n--- EDITAR CONTACTO ---")
    # Reutilizamos lógica de búsqueda simple para encontrar a quien editar
    nombre_buscar = input("Ingrese el nombre exacto del contacto a editar: ")
    
    for contacto in agenda:
        if contacto.nombre.lower() == nombre_buscar.lower():
            print(f"Editando a: {contacto.nombre}")
            
            # Solicitamos nuevos datos. Si deja vacío, mantenemos el actual.
            nuevo_nombre = input(f"Nuevo Nombre [{contacto.nombre}]: ")
            nuevo_tel = input(f"Nuevo Teléfono [{contacto.telefono}]: ")
            nuevo_email = input(f"Nuevo Correo [{contacto.email}]: ")
            nueva_dir = input(f"Nueva Dirección [{contacto.direccion}]: ")

            if nuevo_nombre: contacto.nombre = nuevo_nombre
            if nuevo_tel: contacto.telefono = nuevo_tel
            if nuevo_email: contacto.email = nuevo_email
            if nueva_dir: contacto.direccion = nueva_dir
            
            print(" Contacto actualizado correctamente.")
            return # Terminamos la función al encontrar y editar
            
    print(" No se encontró un contacto con ese nombre.")