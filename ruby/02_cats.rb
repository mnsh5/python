class Gato
  @@especie = 'Felino'  # Variable de clase

  def initialize(nombre, edad)
    @nombre = nombre
    @edad = edad
  end

  def descripcion
    "#{@nombre} tiene #{@edad} años"
  end

  def self.hablar
    "¡Miau!"  # Método de clase
  end

  def self.cambiar_especie(nueva_especie)
    @@especie = nueva_especie  # Método de clase
  end

  def self.especie
    @@especie  # Método de clase
  end
end

# Crear instancias de Gato
gato1 = Gato.new("Luna", 3)
gato2 = Gato.new("Leo", 5)

# Acceder al método de instancia descripcion
puts gato1.descripcion  # Output: Luna tiene 3 años

# Acceder al método de clase hablar
puts Gato.hablar  # Output: ¡Miau!

# Acceder al método de clase cambiar_especie
Gato.cambiar_especie("Gatito")
puts Gato.especie  # Output: Gatito
