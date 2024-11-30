def soma_string(string, caractere ):
    print(caractere)
    print(string)
    if not string:
        return 0
    elif string[0] == caractere:
        return 1 + soma_string(string[1:],  caractere)
    else:
        return soma_string(string[1:],  caractere )
    