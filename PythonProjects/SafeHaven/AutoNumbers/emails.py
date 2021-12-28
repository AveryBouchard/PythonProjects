from PythonProjects.SafeHaven.AutoNumbers.user_info import password
import requests

email = "This is the text I want to send"


def send_simple_message(email_text):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5b4ce196e8f24d008ccf40e7edf32c30.mailgun.org/messages",
            auth=("api", "2125638242b74ab0511b852751c8389d-1831c31e-67f91a2a"),
            data={"from": "Excited User <avery@sandbox5b4ce196e8f24d008ccf40e7edf32c30.mailgun.org>",
                "to": ["averybou@gmail.com", "averydeveloper@gmail.com"],
                "subject": "Hello",
                "text": email_text})


send_simple_message(email)


# import smtplib
#
# from email.mime.text import MIMEText
#
# msg = MIMEText('Testing some Mailgun awesomness')
# msg['Subject'] = "Hello"
# msg['From']    = "postmaster@sandbox5b4ce196e8f24d008ccf40e7edf32c30.mailgun.org"
# msg['To']      = "averydeveloper@gmail.com"
#
# s = smtplib.SMTP('smtp.mailgun.org', 587)
#
# s.login('postmaster@sandbox5b4ce196e8f24d008ccf40e7edf32c30.mailgun.org',
#         'a1c24c94aeed98dc1006406dc7b75a90-1831c31e-f2b6a3c2')
# s.sendmail(msg['From'], msg['To'], msg.as_string())
# s.quit()

# 880af77df8285efbf5f5830b7839cfe5-1831c31e-4fbee398
