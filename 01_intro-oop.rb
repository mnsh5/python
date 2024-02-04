class User
  def initialize(username, country)
    @username = username
    @country = country
  end

  def get_user
    "Hello #{@username} from #{@country}"
  end
end

if __FILE__ == $PROGRAM_NAME
  john = User.new("John", "USA")
  puts john.get_user
end
