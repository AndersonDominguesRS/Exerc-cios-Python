import os

def nav_dir(dir):
    try:
        with os.scandir(dir) as entradas:
            for entrada in entradas:
                print(entrada.path)

                if entrada.is_dir(follow_symlinks=False):
                    nav_dir(entrada.path)
    except PermissionError:
        print("erro de permissão")


