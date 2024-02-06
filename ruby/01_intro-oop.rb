class Cat
  def initialize(name)
    @name = name
  end

  def meow
    puts "#{@name} says: Meoow... 🐈"
  end
end

if __FILE__ == $PROGRAM_NAME
  malala = Cat.new("Malala")
  malala.meow
end
