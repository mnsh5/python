class User
  def initialize(username, country)
    @username = username
    @country = country
  end

  def get_user
    "Hello #{@username} from #{@country}"
  end
end

class Cat
  def initialize(name)
    @name = name
  end

  def greeting
    puts "Hi #{@name}, How is it going?"
  end

  def meow
    puts "My 🐈 #{@name} said Meoow.."
  end
end

if __FILE__ == $PROGRAM_NAME
  john = User.new("John", "USA")
  puts john.get_user

  loli = Cat.new("Loli")
  loli.greeting

  malala = Cat.new("Malala")
  malala.meow
end
