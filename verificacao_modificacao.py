import os
import time

caminho = "."
hoje = time.strftime("%y-%m-%d")

with open("log.txt", "w") as log:
    for arquivo in os.listdir(caminho):
        if arquivo.endswith(".py"):
            modificado = time.strftime("%y-%m-%d", time.localtime(os.path.getmtime(arquivo)))
            if modificado == hoje:
                log.write(f"{arquivo} foi modificado hoje\n")