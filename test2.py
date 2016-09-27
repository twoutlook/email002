import imaplib
import re

from imaplib_connect import open_connection

# list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')
# http://stackoverflow.com/questions/5184483/python-typeerror-on-regex
list_response_pattern = re.compile(b'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')


def parse_list_response(line):
    flags, delimiter, mailbox_name = list_response_pattern.match(line).groups()
    # mailbox_name = mailbox_name.strip('"')
    return (flags, delimiter, mailbox_name)

if __name__ == '__main__':
    c = open_connection()
    try:
        typ, data = c.list()
    finally:
        c.logout()
    print ('Response code:', typ)

    for line in data:
        print ('Server response:', line)
        flags, delimiter, mailbox_name = parse_list_response(line)
        print ('Parsed response:')
        print  (flags, delimiter, mailbox_name)
        
        print ('***mailbox_name:')
        print  (mailbox_name)
        