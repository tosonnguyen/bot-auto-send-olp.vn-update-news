import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


dir_path = os.path.dirname(os.path.realpath(__file__))
load_dotenv(dir_path + '/.env')
dir_path += '/'
gmail_user = os.getenv('GMAIL_USER')
gmail_app_password = os.getenv('GMAIL_APP_PASSWORD')
sent_from = gmail_user
def send_mail():
    with open(dir_path+'mail_list.txt', 'r') as f:
        sent_to = [line.strip() for line in f.readlines()]
    with open(dir_path+'bcc_list.txt', 'r') as f:
        bcc = [line.strip() for line in f.readlines()]
    sent_subject = "[UPDATE] OLP.VN vừa có tin tức mới"
    sent_body = """\
    OLP.vn vừa cập nhật tin tức mới.
    https://www.olp.vn/tin-tức/olympic-icpc/thông-báo

    From small bot with luv! \u2764\ufe0f
    """

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
    print(sent_to)
    msg = MIMEMultipart()
    msg_text = MIMEText(sent_body)
    msg['Subject'] = sent_subject
    msg['From'] = sent_from
    msg['To'] = ", ".join(sent_to)
    msg.attach(msg_text)
    msg.preamble = sent_body


    print(email_text)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to + bcc, msg.as_string().encode('utf8'))
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
    
if __name__ == '__main__':
    send_mail()