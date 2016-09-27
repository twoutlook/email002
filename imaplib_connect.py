import imaplib
import re

# from imaplib_connect import open_connection
# from imaplib_list_parse import parse_list_response
# https://pymotw.com/2/imaplib/


# def parse_list_response(line):
#     list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')
#     flags, delimiter, mailbox_name = list_response_pattern.match(line).groups()
#     mailbox_name = mailbox_name.strip('"')
#     return (flags, delimiter, mailbox_name)

def open_connection(verbose=False):
    hostname = "host411.hostmonster.com"
    username="s1@skyrock-casting.org"
    password="Kunshan@2016"
 
    connection = imaplib.IMAP4_SSL(hostname)
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
        print (c)
        
        typ, data = c.list()
        print ('Response code:', typ)
        print ('Response:',data)
        # # print(data)
        
        # for line in data:
        #     print ('Server response:', line)
        #     # flags, delimiter, mailbox_name = parse_list_response(line)
        #     # print ('Parsed response:', (flags, delimiter, mailbox_name))
        #     flags, delimiter, mailbox_name = parse_list_response(line)
        #     print (c.status(mailbox_name, '(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)'))
        
    finally:
        c.logout()