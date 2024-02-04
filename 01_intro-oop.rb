class Cat
  def initialize(name)
    @name = name
  end

  def meow
    puts "My 🐈 #{@name} said Meoow.."
  end
end

if __FILE__ == $PROGRAM_NAME
  malala = Cat.new("Malala")
  malala.meow
end
