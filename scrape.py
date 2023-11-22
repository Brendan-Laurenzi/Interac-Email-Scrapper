import imaplib
import email
import calendar
from email.header import decode_header

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

    def get_email_data():

        email_user = "prolittle101@hotmail.com"
        email_pass = "8wLdPV_PL5$G5bj"

        mail = imaplib.IMAP4_SSL("outlook.office365.com")
        mail.login(email_user, email_pass)
        mail.select("INBOX")

        email_subject = "INTERAC"
        result, data = mail.search(None, f'SUBJECT "{email_subject}"')

        email_id_list = data[0].split()

        emt_values = []

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

            name = find_string(email_text, "From: ", "<")
            amount = find_string(email_text, "has sent you $", " ")
            memo = find_string(email_text, "Message:\r\n\r\n", "\r")
            date = convert_to_datetime(find_string(email_text, "Sent: ", "\r"))
            refID = find_string(email_text, "Reference Number: ", "\r")

            #url = find_string(email_text, "View in browser<", ">")
            #print(email_text)

            group = (name, amount, memo, date, refID)
            emt_values.append(group)

        mail.close
        mail.logout()

        return emt_values

        #print(emt_values)

if __name__ == "__main__":
    print(emtEmail.get_email_data())