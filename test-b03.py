import base64
import email
import imaplib
import imaplib_connect
from email.parser import HeaderParser
from imaplib_list_parse import parse_list_response
from email.header import decode_header
# https://docs.python.org/3/library/email.header.html
M = imaplib_connect.open_connection()

M.select()
typ, data = M.search(None, 'ALL')

messages = []
messageInfo = {}

# http://www.tutorialspoint.com/python/string_find.htm



for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    
    message = data[0][1]
    raw_message=message.decode("utf-8")
    msg =  email.message_from_string(raw_message)

    print(num," ==> ",msg['Subject'])
    messageInfo['subject'] = msg['Subject']	    
    # print(num, messageSubject)
    # print()
    # print(num.decode('ascii'), )
    to_decode = decode_header( messageInfo['subject'] )
    print("to_decode XXX")
    print(to_decode)
          
        
    # if ("=?UTF-8?" in messageInfo['subject'] ):
        # messageSubject=messageSubject.decode('GBK')
        # messageSubject=messageSubject.decode('ascii')
        
   
    to_decode = decode_header( messageInfo['subject'] )
    print("to_decode ///")
    print(to_decode)
    desired_subject=""
    for x in to_decode:
        # print(    "    ",x)
        # print( "    ---",x[0])
        # print( "    ---",x[1])
        if (x[1] == None):
            if (type(x[0])=='str'):
                pass
            else:
                x[0]=x[0].decode("ascii")
            desired_subject += x[0]
        else:
            # print(x[0].decode(x[1]))
            desired_subject += x[0].decode(x[1])
    print(desired_subject)
    print()
    
    