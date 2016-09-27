import email
import imaplib
import imaplib_connect
from email.parser import HeaderParser
from imaplib_list_parse import parse_list_response

c = imaplib_connect.open_connection()



try:
    print ("要能 scan 中文  ")
    
    typ, mailbox_data = c.list()
    for line in mailbox_data:
        flags, delimiter, mailbox_name = parse_list_response(line)
        c.select(mailbox_name, readonly=True)
        typ, msg_ids = c.search(None, '(SUBJECT "daily testing")')
        # typ, msg_ids = c.search(None, u'(SUBJECT "中文")')
        # UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
        print (mailbox_name, typ, msg_ids)   
        
        
     
        
finally:
    try:
        c.close()
    except:
        pass
    c.logout()