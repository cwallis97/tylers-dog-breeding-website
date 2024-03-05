import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, phone, note):
  sender_email = "smtp@gmail.com"
  receiver_email = "christianmwallis@gmail.com"
  smtp_server = "smtp.gmail.com"
  password = os.environ['PASSWORD']
  port = 465
  print


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
      <p>Dear, Dog Enthusiast<br>
        Thank you for visiting our website! we appreciate your interest in our furry friends, If you have any questions about dog breeds, training tips, or anything else related to dogs, we are always happy to help.  <br>
       
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