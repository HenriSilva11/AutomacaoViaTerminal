import os

print("diretório ataul: ", os.getcwd())

arquivos = os.listdir()

print("arquivos e pastas aqui: ", arquivos)

#executando e capturando retorno
import subprocess

resultado = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print("saida do comando: ", resultado.stdout)

#verificar status

comando = subprocess.run(["ping", "-n", "1", "google.com"])

if comando.returncode == 0:
    print("conexão ativa!")
else:
    print("sem conexão com a internet. ")





