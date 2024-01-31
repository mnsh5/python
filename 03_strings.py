"""
Strings
This file talks about strings.
"""

string_with_quotes = "Hello, it's me."
print(string_with_quotes)

another_with_quotes = 'He said "You are amazing!", yesterday.'
print(another_with_quotes)

multiline = """Hello, it's me.
Jose Salvatierra.
"""
print(multiline)

"""
Python String formatting.
"""
name = "Jose Salvatierra"
greeting = f"How are you, {name}?"
print(greeting)

username = "Bob"
final_greeting = "How are you, {}?"
username_greeting = final_greeting.format(username)
print(username_greeting)
