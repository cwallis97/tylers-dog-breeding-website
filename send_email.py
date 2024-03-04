import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "smtp@gmail.com"
receiver_email = "beckygarding@gmail.com"
smtp_server = "smtp.gmail.com"
password = os.environ['PASSWORD']
port = 465



message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email


message["Subject"] = "multipart test"


text = """\
Hey there,
This message is sent from Python."""


html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""



part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login("threads4pups@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message.as_string())
