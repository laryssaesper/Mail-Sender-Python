import smtplib

email=str(input("Remetente: "))
emailDestino=str(input("Destinatário: "))

assunto=str(input("Assunto: "))
corpo=str(input("Corpo: "))

mensagem=f"Subject: {assunto}\n\n{corpo}"

server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "senha")

server.sendmail(email, emailDestino, mensagem)

print("E-mail enviado com sucesso para: ", emailDestino)
