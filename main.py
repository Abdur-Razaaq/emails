import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'zakjardien23@gmail.com'
receiver_email = ["jchno116012003@gmail.com", "Thapelo@lifechoices.co.za", "kamogelomkonto01@gmail.com"]
password = input("Enter senders email password: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Multipart Test"
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)

a_message = """\
Hello
i
y
"""

part1 = MIMEText(a_message, "plain")

message.attach(part1)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
