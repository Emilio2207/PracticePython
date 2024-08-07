# Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Emilio", "Ramirez", "emilioDev", 35
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)

# Cambiamos su tipo
new_name = 35
new_age = "Emilio"

print(new_name)
print(new_age)

# Formzamos su tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))

