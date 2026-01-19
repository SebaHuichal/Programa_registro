# --- ARCHIVO: main.py ---
## Creamos el archivo principal, este será el cerebro del problema.
from agrega import agregar_contacto
from busca import buscar_contacto
from edita import editar_contacto
from elimina import eliminar_contacto
from datos import mostrar_contactos



def main():
    agenda = [] 

    # 2. AGREGAMOS LA OPCIÓN AL DICCIONARIO
    opciones_menu = {
        "1": agregar_contacto,
        "2": buscar_contacto,
        "3": editar_contacto,
        "4": eliminar_contacto,
        "5": mostrar_contactos  
    }

    print("¡Bienvenido al Sistema de Gestión de Contactos!")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Ver todos los contactos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Cerrando el sistema. ¡Hasta luego!")
            break
        
        if opcion in opciones_menu:
            funcion_seleccionada = opciones_menu[opcion]
            funcion_seleccionada(agenda)
        else:
            print(" Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()