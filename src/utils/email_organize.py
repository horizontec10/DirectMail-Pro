from core.email_service import EmailSender, EmailBuilder
from utils.file_handler import get_email_list
from flask import request


def process_email_submission() -> str:
    body_text = request.form.get("body_text")
    day_shift = request.form.get("day_shift")
    name_employee = request.form.get("name_employee")
    position = request.form.get("position")

    # Informações do cliente
    mode = request.form.get("mode")

    if mode == "single":
        recipients = list(request.form.get("recipient"))
    else:
        recipients = get_email_list()

    subject = request.form.get("subject")

    email_builder = EmailBuilder(
        name_employee=name_employee,
        position=position,
        day_shift=day_shift,
        body_text=body_text
    )
    body_email = email_builder.body_email()
    
    email_sender = EmailSender()
    for recipient in recipients:
        email_sender.send(
            recipient=recipient,
            subject=subject,
            body_email=body_email
        )
    return "As informações enviadas para o(s) e-mail(s) com sucesso!"
    
