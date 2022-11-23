
import smtplib
from email.message import EmailMessage
import configparser

def send_email(self, err_msg):
    cf = configparser.ConfigParser()
    cf.read("fmssimdata.ini")
    EMAIL_ADDRESS = cf.get('settings','EMAIL_ADDRESS')
    EMAIL_PASS = cf.get('settings','EMAIL_PASS')
    to = cf.get('settings','TO')

    msg = EmailMessage()
    msg['Subject'] = 'This is a reminder'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to 
    msg.set_content(err_msg)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
            smtp.send_message(msg)
    except:
        print("email does not send")
            


if __name__ == "__main__":
    send_email("this is error msg")