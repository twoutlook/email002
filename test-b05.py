import base64
import email
import imaplib
import imaplib_connect
from email.parser import HeaderParser
from imaplib_list_parse import parse_list_response
from email.header import decode_header
# https://docs.python.org/3/library/email.header.html
# https://docs.python.org/3/library/email-examples.html


M = imaplib_connect.open_connection()

M.select()
typ, data = M.search(None, 'ALL')

messages = []
messageInfo = {}

# http://www.tutorialspoint.com/python/string_find.htm



for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    
    message = data[0][1]
    
    # bytes to string, 
    raw_message=message.decode("utf-8")
    
    msg =  email.message_from_string(raw_message)
    messageInfo['subject'] = msg['Subject']	    

    to_decode = decode_header( messageInfo['subject'] )
    desired_subject=""
    for x in to_decode:
        # print(    "    ",x)
        # print( "    ---",x[0])
        # print( "    coding:",x[1])
        if (x[1] == None):
            # WHY, 有時候是bytes, 有時候是string? 
            if isinstance(x[0], str):
                desired_subject += x[0]
            else:
                desired_subject += x[0].decode("ascii")
        else:
            desired_subject += x[0].decode(x[1])
        print(num.decode("ascii"),desired_subject)
        
        # if (x[1] == None):
        #     # desired_subject += x[0].decode("ascii")
            
        # else:
            # desired_subject += x[0].decode(x[1])
    # print(desired_subject)
    # print()
    
    