import smtplib

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login('email address', 'password')
server.sendmail('from email address', 'to email address', 'Subject: Test \
    \nTest email.')
server.quit()

# Send text message through SMS gateway of destination number
# server.sendmail('xxxxx@gmail.com', 'xxxxxxxxxx@messaging.sprintpcs.com', 'Hello') # Text message

# Need to enable less secure apps to access your Google account for this to work