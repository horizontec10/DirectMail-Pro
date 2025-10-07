from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from exceptions import EmailTemplateInvalidException, EmailSendException
from config.constants import (
    EMAIL_PASSWORD,
    EMAIL_PORT,
    EMAIL_SMTP_SERVER,
    EMAIL_SERVER,
    EMAIL_SENDER,
    TEMPLATES_HORIZONTEC
)

# Classe para construção do Email
class EmailBuilder:
    def __init__(self, name_employee: str, position: str = "Vendedor", day_shift: str = "Bom dia!", body_text: str = ""):
        self.name_employee = name_employee
        self.position = position
        self.day_shift = day_shift
        self.body_text = body_text if body_text is not None else EmailTemplateInvalidException("Erro ao enviar as informações do e-mail para o cliente.")

    def body_email(self):
        env = Environment(loader=FileSystemLoader(TEMPLATES_HORIZONTEC))
        template = env.get_template("commercial_horizontec.html")

        return template.render(
            name_employee=self.name_employee,
            position=self.position,
            day_shift=self.day_shift,
            body_text=self.body_text
        )
    
# Classe para envio do Email
class EmailSender:
    def __init__(self):
        self._email_password = EMAIL_PASSWORD
        self._email_port = EMAIL_PORT
        self._email_smtp_server = EMAIL_SMTP_SERVER
        self._email_server = EMAIL_SERVER
        self._email_sender = EMAIL_SENDER

    def send(self, recipient: str, subject: str, body_email: str) -> None:
        try:
            message = MIMEMultipart()
            message["From"] = self._email_sender
            message["To"] = recipient
            message["Subject"] = subject
            
            message.attach(MIMEText(body_email, "html"))

            server = SMTP_SSL(self._email_smtp_server, self._email_port)
            server.login(self._email_server, self._email_password)
            server.send_message(message)
            server.quit()
            return 
        except Exception as e:
            raise EmailSendException(f"Erro ao enviar o e-mail: {str(e)}")

