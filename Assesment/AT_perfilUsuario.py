perfils = {}

def perfil_usuario(nome_usuario, nome, idade):
    perfils[nome_usuario] = {

        "nome": nome,
        "idade": idade ,
    }

def buscar_perfils(nome_usuario ):
    if nome_usuario in perfils:
        return perfils[nome_usuario]
    else:
        return None