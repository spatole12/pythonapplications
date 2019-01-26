from email.mime.text  import MIMEText
# to make message html enabled
import smtplib

def send_email(email,height,average_height,count):
    from_email="shivu.tec12@gmail.com"
    from_password="shivani@123"
    to_email=email

    subject="Height survey"
    message="Hey, your height is <strong> %s </strong>.<br>Your average height is %s, considering other <strong> %s </strong> individuals" %(height,average_height,count)

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
