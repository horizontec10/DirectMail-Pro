from flask import request

def get_email_list() -> list:
    file = request.files.get("csv_file")
    recipients = []

    if not file:
        raise Exception("Não foi encontrado nenhuma arquivo enviado.")
    
    lines = file.stream.read().decode("utf-8").splitlines()

    for line in lines:
        email = line.strip()
        if email and "email" not in email.lower():
            recipients.append(email)
    
    return recipients