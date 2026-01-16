### Aca definimos la segunda funcion de nuestro programa.
### Definiremos la opcion 2 (en nuestro main).

def buscar_contacto(agenda):

    ### Aca llamaremos lower para poder buscar de mejor maner .
    ### en python las O es distinto a o.
    
    print("\n--- BUSCAR CONTACTO ---")
    buscar = input("Ingrese Nombre o Teléfono a buscar: ").lower()
    estado = False

    for contacto in agenda:
        
        if buscar in contacto.nombre.lower() or buscar == contacto.telefono:
            print("-----------------------------")
            print(contacto) 
            print("-----------------------------")
            estado = True
    
    if not estado:
        print(" No se encontraron coincidencias.")