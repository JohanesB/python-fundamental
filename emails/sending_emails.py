import smtplib
import getpass
smtb_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtb_object.ehlo())
print(smtb_object.starttls())

email = getpass.getpass("Email: ")
password = getpass.getpass("password: ")
smtb_object.login(email, password)

from_address = email
to_address = email
subject = input("Enter the subject line: ")
message = input("Enter the body message: ")
msg = "Subject: "+ subject + "\n" + message
smtb_object.sendmail(from_address, to_address, msg)
