import base64
import email
import imaplib
import imaplib_connect
from email.parser import HeaderParser
from imaplib_list_parse import parse_list_response
from email.header import decode_header
# https://docs.python.org/3/library/email.header.html
prefix = '=?UTF-8?'
suffix = '?='

M = imaplib_connect.open_connection()

M.select()
typ, data = M.search(None, 'ALL')

messages = []
messageInfo = {}

# http://www.tutorialspoint.com/python/string_find.htm



for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    
    message = data[0][1]

    
     ### TO
    # message = message.replace('Delivered-To:', '')  # so the next find isn't confused

    # messageToPos = message.find('To: ')
    # endPos = message.find('\n', messageToPos)
    # messageTo = message[messageToPos + 3:endPos].strip() 
    
    # if messageTo.find(' 0:
    # 	messageTo = messageTo.split('', '')

    # messageInfo['to'] = messageTo

    # https://www.sitekickr.com/snippets/python/retrieve-messages-imap-account
    # http://stackoverflow.com/questions/5259601/how-convert-email-subject-from-utf-8-to-readable-string
    #SUBJECT
    # messageSubjectPos = message.find(b'Subject: ')
    
    # endPos = message.find('\n', messageSubjectPos)
    # endPos = message.find(b'\n', messageSubjectPos)
    
    # http://stackoverflow.com/questions/14773732/python-email-parser-extract-header-from-email
    # messageSubject = message[messageSubjectPos + 9:endPos].strip() 
    raw_message=message.decode("utf-8")
    msg =  email.message_from_string(raw_message)
    print(msg['Subject'])
    messageInfo['subject'] = msg['Subject']	    
    # print(num, messageSubject)
    print()
    print(num.decode('ascii'), )
   
        
    if ("=?UTF-8?" in messageInfo['subject'] ):
        # messageSubject=messageSubject.decode('GBK')
        # messageSubject=messageSubject.decode('ascii')
        
   
        to_decode = decode_header( messageInfo['subject'] )
        # print(to_decode)
        desired_subject=""
        for x in to_decode:
            # print(    "    ",x)
            # print( "    ---",x[0])
            # print( "    ---",x[1])
            if (x[1] == None):
                # print(x[0].decode("ascii"))
                desired_subject += x[0].decode("ascii")
            else:
                # print(x[0].decode(x[1]))
                desired_subject += x[0].decode(x[1])
        print(desired_subject)
        
    