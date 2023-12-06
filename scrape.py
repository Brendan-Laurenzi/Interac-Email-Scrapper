import imaplib2
import email
import calendar
from email.header import decode_header
from datetime import datetime, timedelta

def find_string(text, searchcase, endcase):
    index = text.find(searchcase)
    string = ""
    if index == -1:
        return "N/A"
    else:
        index += len(searchcase)
        while (text[index] != endcase):
            string += text[index]
            index += 1
    return string

# Convert (Oct 5, 2023 2:20 PM) -> (2023-10-05 14:20:00)
def convert_to_datetime(date): 
    # Extract Year
    index = date.find("20")
    datetime = date[index:index+4]

    # Extract Month
    month_abbr = date[0:3]
    month_num = list(calendar.month_abbr).index(month_abbr)
    if month_num < 10:
        datetime += "-0" + str(month_num)
    else:
        datetime += "-" + str(month_num)

    # Extract Day
    index = date.find(",")
    if date[index-2] == " ":
        datetime += "-0" + date[index-1:index]
    else:
        datetime += "-" + date[index-2:index]

    # Extract Hours
    index = date.find(":")
    hour = int(date[index-2:index])
    if date.find("PM") > 0:
        hour += 12
        datetime += " " + str(hour)
    elif date[index-2] == " ":
        datetime += "0" + str(hour)
    else:
        datetime += str(hour)

    # Extract Minuites
    datetime += ":" + date[index+1:index+3] + ":00"

    return datetime

class emtEmail:

    def __init__(self):
        self.emailUser = "prolittle101@hotmail.com"
        self.emailPass = "8wLdPV_PL5$G5bj"
        self.mailServer = "outlook.office365.com" # HOTMAIL EMAIL SERVER
        self.mailBox = "Interac"
        self.emailSubject = "interac e-transfer"
        self.mail = None
        self.emailIDList = None

    def connect(self):
        self.mail = imaplib2.IMAP4_SSL(self.mailServer)
        try:
            self.mail.login(self.emailUser, self.emailPass)
        except imaplib2.IMAP4.error as e:
            print("Email Error:", e)

    def disconnect(self):
        try:
            self.mail.close
            self.mail.logout()
        except imaplib2.IMAP4.error as e:
            print("Email Error:", e)

    def get_email_count(self, condition=None):
        try:
            self.mail.select(self.mailBox)
            if condition:
                result, data = self.mail.search(None, f'{condition} SUBJECT "{self.emailSubject}"')
            else:
                result, data = self.mail.search(None, f'SUBJECT "{self.emailSubject}"')
            self.emailIDList = data[0].split()
            return (len(self.emailIDList))
        except imaplib2.IMAP4.error as e:
            print("Email Error:", e)

    def fetch_email_content(self, index):
        try:
            result, message_data = self.mail.fetch(self.emailIDList[index], "(RFC822)")
            # Parse the email content
            raw_email = message_data[0][1]
            email_message = email.message_from_bytes(raw_email)

            received_date = email.utils.parsedate(email_message.get("Date"))

            # Extract the email text
            email_text = ""
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    email_text = part.get_payload(decode=True).decode(part.get_content_charset(), errors="ignore")

    
            if (email_text.find('The money transfer you sent') != -1) or (email_text.find('(CAD) you sent to') != -1): return -1
            #print("="*100)
            #print(email_text)

            # FORWARDED EMAIL PROCCESSING
            if email_message.get("Subject").lower().find("fw:") != -1:
                
                name = find_string(email_text, "From: ", "<")
                amount = find_string(email_text, "has sent you $", " ").replace(',', '')
                memo = find_string(email_text, "Message:\r\n\r\n", "\r")
                date = convert_to_datetime(find_string(email_text, "Sent: ", "\r"))
                refID = find_string(email_text, "Reference Number: ", "\r")

            # NON-FORWARDED EMAIL PROCCESSING
            else:
                # Older E-Transfers / no AutoDeposit do not have a reference number -> skip email
                refID = find_string(email_text, "Reference Number: ", "\r")
                if refID == 'N/A': return -1

                name = find_string(email_text, ",\r\n\r\n", "h").strip()
                amount = find_string(email_text, "of $", " ").replace(',', '')
                memo = find_string(email_text, "Message:\r\n", "\r")
                date = f"{received_date[0]}-{received_date[1]}-{received_date[2]} {received_date[3]}:{received_date[4]}:{received_date[5]}"

                if memo == "": memo = 'N/A'

            return (name, amount, memo, date, refID)

        except imaplib2.IMAP4.error as e:
            print("Email Error:", e)


    def check_for_new_emails(self):
        try:
            self.mail.select(self.mailBox)
            # Idle for 5 seconds listening for new event in selected Inbox
            self.mail.idle()
            # Check wether the response was an event or a timeout
            response = self.mail.response('IDLE')
            if response[1] == [None]:
                return 1
            else:
                return 0
                    
        except imaplib2.IMAP4.error as e:
            print("Email Error:", e)
            return -1
            

    def break_idle_loop(self):
        try:
            self.connect()

            self.get_email_count()
            self.mail.store(self.emailIDList[0], '-FLAGS', '(\Seen)')
            self.mail.store(self.emailIDList[0], '+FLAGS', '(\Seen)')

            self.disconnect()
                    
        except imaplib2.IMAP4.error as e:
            print("Email Error:", e)





if __name__ == "__main__":
    scraper = emtEmail()
    scraper.connect()
    #scraper.check_for_new_emails()

    count = scraper.get_email_count('UNSEEN')
    print(count)
    for index in range(count):
        print(scraper.fetch_email_content(index))

    scraper.disconnect()