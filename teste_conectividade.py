
import os
import subprocess
from email.mime.text import MIMEText
import smtplib

#executando e capturando retorno
import subprocess

ping = subprocess.run(["ping", "google.com"], capture_output=True, text=True)
resultado_ping = ping.stdout

#verificar status e printar no terminal

if ping.returncode == 0:
    print("conexão ativa!", ping.stdout)
else:
        print("sem conexão!", ping.stdout)

#envio para email

email_remetente = "SEU_EMAIL"
senha_remetente = "SUA_SENHA"
email_destino = "EMAIL_DESTINO"

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
   print("Email enviado com sucesso!")
except Exception as e:
    print("Erro ao enviar o email: ", e)






