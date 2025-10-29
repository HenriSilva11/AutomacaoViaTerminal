
import os
import subprocess
from email.mime.text import MIMEText
import smtplib

#executando e capturando retorno
import subprocess

ping = subprocess.run(["ping", "google.com"], capture_output=True, text=True)
resultado_ping = ping.stdout

print("saida do comando: ", ping.stdout)

#envio para email

email_remetente = "pequenohenri72@gmail.com"
senha_remetente = "nufr mcxw cptt towj"
email_destino = "victorribeirodesouza10@gmail.com"

msg = MIMEText(f"Resultado do ping:\n\n{resultado_ping}")
msg["subject"] = "Resultado do ping"
msg["from"] = email_remetente
msg["to"] = email_destino

try: 
   server = smtplib.SMTP("smtp.gmail.com", 587)
   server.starttls()
   server.login(email_remetente, senha_remetente)
   server.send_message(msg)
   server.quit()
except Exception as e:
    print("Erro ao enviar o email: ", e)


#verificar status e printar no terminal

comando = subprocess.run(["ping", "-n", "1", "google.com"])

if comando.returncode == 0:
    print("conexão ativa!")
else:
    print("sem conexão com a internet. ")

