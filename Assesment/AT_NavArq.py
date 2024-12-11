import os

def listar_arquivos(diretorio):
    if not os.path.exists(diretorio):
        print("Diretório não localizado")
        return
    for item in os.listdir(diretorio):
        patch = os.path.join(diretorio, item)
        if os.path.isdir(patch):
            listar_arquivos(patch)
        elif os.path.isfile(patch):
            print(patch)



diretorio_inicial = "C:/Users" 
listar_arquivos(diretorio_inicial)