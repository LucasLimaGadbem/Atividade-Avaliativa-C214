import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_user = os.getenv("SMTP_USER")
smtp_pass = os.getenv("SMTP_PASS")
mail_to = os.getenv("MAIL_TO")

msg = MIMEMultipart()
msg["From"] = smtp_user
msg["To"] = mail_to
msg["Subject"] = "Notificação CI/CD"

body = "Pipeline executado com sucesso!"
msg.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(smtp_user, mail_to, msg.as_string())
