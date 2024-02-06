# Imagina que tienes un montón de gatitos y quieres enseñarles a maullar.
# Hay una forma de enseñarles a todos a maullar al mismo tiempo, sin necesidad de saber cuál es el nombre de cada uno.
# Esa es la función de staticmethod.

# Ahora, imagina que quieres enseñarles una nueva forma de maullar que es exclusiva para todos los gatos de una misma familia.
# Tienes diferentes familias de gatos, pero cada una tiene su propio maullido especial.
# En este caso, usas classmethod.

class Gato:
    # Definimos una función para enseñarles a todos los gatos a maullar igual.
    @staticmethod
    def maullar():
        return "¡Miau!"

    # Definimos una función para enseñarles a todos los gatos de una familia a maullar igual.
    @classmethod
    def maullido_especial(cls):
        if cls == Siames:
            return "¡Miau Siames!"
        elif cls == Persa:
            return "¡Miau Persa!"
        else:
            return "¡Miau!"

# Creamos diferentes tipos de gatos
class Siames(Gato):
    pass

class Persa(Gato):
    pass

# Todos los gatos pueden maullar igual
print(Gato.maullar())  # Output: ¡Miau!

# Pero cada tipo de gato de una familia puede tener su propio maullido especial
print(Siames.maullido_especial())  # Output: ¡Miau Siames!
print(Persa.maullido_especial())   # Output: ¡Miau Persa!
