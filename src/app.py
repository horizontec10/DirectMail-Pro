from src.core.email_service import EmailSender, EmailBuilder
from src.utils.file_handler import get_email_list
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
        return jsonify({"response": "As informações enviadas para o(s) e-mail(s) com sucesso!", "status": True}), 201
    except Exception as e:
        return jsonify({"response": f"Erro ao enviar o e-mail: {str(e)}", "status": False}), 401

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)