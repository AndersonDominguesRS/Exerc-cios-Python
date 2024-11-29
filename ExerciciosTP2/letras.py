string_teste = "Sítio do pica-pau amarelo \n 2023"

def print_string(string):
    return [char for char in string if char != ' ' and char != '\n']


print (print_string(string_teste))