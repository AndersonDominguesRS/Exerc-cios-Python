def verifica_palavra(palavra):
    print(palavra)
    palavra = palavra.replace( " " , "" ).lower()   

    def verificar(p, inicio, fim ):
        if inicio >= fim:
            return True

        if p[inicio] != p[fim ]:
            return False
        return verificar(p, inicio + 1, fim - 1)
    return verificar(palavra, 0, len( palavra) - 1)