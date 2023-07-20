import imaplib
import getpass

M = imaplib.IMAP4_SSL('smtp.gmail.com')
email = getpass.getpass("Email: ")
passwd = getpass.getpass("Password: ")

M.login(email, passwd)
print(M.list())
print(M.select('INBOX'))

typ, data = M.search(None, 'FROM email')
print(typ)
print(data)

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
print(email_data)

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

import email # helps to grab the actual message from the string
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
