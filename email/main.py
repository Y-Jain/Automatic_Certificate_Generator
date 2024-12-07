import pandas as p
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
data = p.read_csv(r"C:\Users\HP\OneDrive\Desktop\design\email\certificates.csv")
# print(type(data))
email_col = data.get("Email")
list_of_emails = list(email_col)
print(list_of_emails)
try:
    server = sm.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("yashj17033@gmail.com","Dada@91311")
    from_ = "yashj17033@gmail.com"
    to_ = list_of_emails
    message = MIMEMultipart("alternative")
    message['Subject'] = "This is just testing"
    message["from"] = "yashj17033@gmail.com"

    html ='''
    <html>
    <head>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </head>
    </html>
    '''
    part2 = MIMEText(html,"html")
    message.attach(part2)
    server.sendmail(from_,to_,message.as_string())
    print("message has been send successfully")

except Exception as e:
    print(e)