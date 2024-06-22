import smtplib
from email.message import EmailMessage

def send_email(subject, body, receiver_email):
    sender_email = "eirprimeconsole@outlook.com" 
    password = "Open_1234" 

    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
