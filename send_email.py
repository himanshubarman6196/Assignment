import smtplib
import ssl
from email.message import EmailMessage
import logging

logging.basicConfig(level = logging.INFO)

""" global variables for smtp """
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "Enter the sender email address" 

password = "Enter the password of send address"

""" for tracking event """
import logging

logging.basicConfig(level = logging.INFO)


class SendMail:

    def send_mail(message,recipient):
        try:
            context = ssl.create_default_context()
            smtpObj = smtplib.SMTP(host=smtp_server, port=port)
            smtpObj.starttls(context=context)
            smtpObj.login(sender_email,password)
            smtpObj.sendmail(sender_email, recipient, message)
            logging.info(f'Email Sent!')
        except Exception as e:
            print(f"Error: unable to send email due to {e}")




if __name__ == '__main__':
    logging.info(f'Please enter the sender email and password in the script before executing and allow less secure app on google account')
    subject = input("Please enter the subject - >")
    body = input("Please enter the body - >")
    recipient = input("Please enter the subject - >")

    message = f""" Subject: {subject}

    {body}"""

    SendMail.send_mail(message,recipient)




