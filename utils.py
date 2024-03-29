import datetime
import smtplib
from email.mime.text import MIMEText


# Função pra criação de log
def log_request(request, response):
    try:
        with open("log.txt", "a") as log_file:
            current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            ip_address = request.remote_addr
            request_content = request.data.decode('utf-8')
            response_content = response.get_data(as_text=True)
            log_entry = f"{current_time} - IP: {ip_address}\nRequest Content:\n{request_content}\nResponse Content:\n{response_content}\n\n"
            log_file.write(log_entry)
    except Exception as e:
        # Em caso de erro ao registrar o log, você pode optar por fazer algum tratamento específico ou simplesmente ignorá-lo.
        pass


def mail():
    print("Entrando na função mail")
        # Dados de autenticação
    username = "seu-email"
    password = "sua-senha"
    emailDestino = "destino"
    conteudo = "Erro com a APi"
    # Criação do objeto MIMEText
    msg = MIMEText(conteudo, 'plain', 'utf-8') # é necessário codificar o objeto para utf-8 para poder enviar acentos
    msg['To'] = emailDestino
    msg['From'] = username
    msg['Subject'] = "Erro com a API"

    # Adicionando cabeçalhos de conteúdo
    msg.add_header('Content-Type', 'text/plain; charset=UTF-8')

    # Enviando o e-mail
    with smtplib.SMTP("smtp.hostinger.com", 465) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, emailDestino, msg.as_string())

    print("E-mail enviado com sucesso!")