import imaplib
import email
from email.header import decode_header

# Your email and password
email_user = "prolittle101@hotmail.com"
email_pass = "8wLdPV_PL5$G5bj"

# Connect to the IMAP server (Gmail in this example)
mail = imaplib.IMAP4_SSL("outlook.office365.com")

# Log in to your email account
mail.login(email_user, email_pass)

# Select the mailbox you want to work with (e.g., "INBOX" for your inbox)
mail.select("INBOX")

# Search for the email you want (e.g., by subject)
email_subject = "INTERAC"
result, data = mail.search(None, f'SUBJECT "{email_subject}"')

# Get the list of email IDs that match the search criteria
email_id_list = data[0].split()

# Assuming you want to fetch the first email that matches the criteria
for email_id in email_id_list:
    result, message_data = mail.fetch(email_id, "(RFC822)")

    # Parse the email content
    raw_email = message_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Extract the email text
    email_text = ""

    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            email_text = part.get_payload(decode=True).decode(part.get_content_charset(), errors="ignore")

    print("Email text:")
    print(email_text)
    print("="*100)

# Close the mailbox and log out
mail.close
mail.logout()