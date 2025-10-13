from src.core.email_service import EmailSender, EmailBuilder
from src.utils.file_handler import get_email_list
from src.services.email_service import EmailService
from src.dto.email_dtos import EmailCreateDTO, EmailFilterDTO
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
email_service = EmailService()

@app.route("/", methods=["GET"])
def index():
    return render_template("form.html")

@app.route("/send-email", methods=["POST"])
def process_email_submission() -> str:
    body_text = request.form.get("body_text")
    day_shift = request.form.get("day_shift")
    name_employee = request.form.get("name_employee")
    position = request.form.get("position")
    # Informações do cliente
    mode = request.form.get("mode")


    if mode == "single":
        recipients = [request.form.get("recipient")]
    else:
        recipients = get_email_list()

    subject = request.form.get("subject")
    try:
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
            email_create = EmailCreateDTO(
                email=recipient,
                subject=subject,
                body_email=f"{day_shift}\n{body_text}",
                position_employee=position,
                name_employee=name_employee
            )
            reponse_email = email_service.create(email_create_dto=email_create)
        return jsonify({"response": f"{reponse_email.model_dump()}", "status": True}), 201
    except Exception as e:
        return jsonify({"response": str(e), "status": False}), 401

if __name__ == "__main__":

    app.run("0.0.0.0", debug=True, port=8080)