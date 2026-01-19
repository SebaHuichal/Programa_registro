import unittest
from datos import Contacto

class TestAgenda(unittest.TestCase):

    def test_datos_contacto(self):
        # Igual que el ejemplo 'test_upper' de la guía
        # Creamos un contacto de prueba
        persona = Contacto("Seba", "12345", "seba@gmail.com", "San Fernando")
        
        # Verificamos que los datos sean iguales a lo esperado (assertEqual)
        self.assertEqual(persona.nombre, "Seba")
        self.assertEqual(persona.telefono, "12345")
        self.assertEqual(persona.email, "seba@gmail.com")

    def test_formato_texto(self):
        # Probamos que el __str__ devuelva el formato correcto con las barras separadoras
        persona = Contacto("Ana", "999", "ana@test.com", "Sur")
        texto_esperado = "Ana | Tel: 999 | Email: ana@test.com | Dir: Sur"
        
        self.assertEqual(str(persona), texto_esperado)

if __name__ == '__main__':
    unittest.main()