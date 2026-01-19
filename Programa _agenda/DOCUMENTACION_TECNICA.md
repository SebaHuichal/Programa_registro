# Documentación Técnica: Sistema de Gestión de Contactos

**Proyecto:** Sistema de Gestión de Contactos
**Autor:** Sebastián Huichal


## 1. Introducción.
Este documento describe la arquitectura, estructura y funcionamiento del "Sistema de Gestión de Contactos". Es una aplicación de consola diseñada para administrar una agenda personal, permitiendo crear, leer, actualizar y eliminar registros de manera persistente en memoria durante la ejecución.

## 2. Arquitectura del Software.
El proyecto sigue un patrón de **Diseño Modular** y **Programación Orientada a Objetos (POO)**. La lógica se ha distribuido en módulos especializados para facilitar el mantenimiento y la actualizacion.

### Principios aplicados:
* **Encapsulamiento:** Uso de la clase `Contacto` para modelar los datos.
* **Separación de Responsabilidades:** Cada archivo `.py` cumple una función única.
* **Modularidad:** Uso de importaciones para conectar los componentes.

## 3. Estructura del Proyecto.
El código fuente se organiza dentro del directorio `Programa_agenda` de la siguiente manera:

```text
Programa_registro/
└── Programa_agenda/    # Carpeta del Código Fuente
    ├── Main.py         # Punto de entrada y menú principal
    ├── datos.py        # Clase Contacto y estructura de datos
    ├── agrega.py       # Lógica para insertar registros
    ├── busca.py        # Lógica de búsqueda (nombre/teléfono)
    ├── edita.py        # Lógica de modificación de atributos
    ├── elimina.py      # Lógica de borrado seguro
    └── test_agenda.py  # TESTING
```
## 4. Descripción Detallada de Módulos.
### 4.1. datos.py (El Modelo).

Contiene la definición de la clase base.

 Clase Contacto: Define los atributos `nombre, telefono, email y direccion`.

 Método __str__: Sobrecarga la representación en texto para devolver una cadena formateada legible (Nombre | Tel | Em | Dir).

### 4.2. Main.py (El Controlador).

Es el orquestador del sistema.
 Inicializa la lista principal agenda = [].
Implementa un Diccionario de Funciones `(opciones_menu)` para gestionar el flujo de control sin abusar de condicionales `if/else`.
Mantiene el ciclo de vida de la aplicación `(while True)`.

### 4.3. Módulos Funcionales.
`agrega.py`: Solicita inputs al usuario, instancia el objeto `Contacto` y lo añade a la lista.

`busca.py`: Recorre la lista comparando cadenas de texto. Implementa `.lower()` para búsquedas insensibles a mayúsculas.

`edita.py`: Permite buscar un contacto y reescribir sus atributos. Si el usuario deja un campo vacío, se conserva el dato original.

`elimina.py`: Busca un contacto y solicita confirmación (s/n) antes de removerlo permanentemente de la lista usando `.pop()`.