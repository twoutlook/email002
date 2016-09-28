import sys,traceback
import base64
import email
import imaplib
import imaplib_connect
from email.parser import HeaderParser
from email.parser import Parser

from imaplib_list_parse import parse_list_response
from email.header import decode_header


def mark001_decode(src):
    d = decode_header( src )
    # for d1 in d:
    #     print (d1)
    
    to_decode = decode_header( src )
    desired_subject=""
    for x in to_decode:
        # print(    "    ",x)
        # print( "    ---",x[0])
        # print( "    coding:",x[1])
        if (x[1] == None):
            # WHY, 有時候是bytes, 有時候是string? 
            if isinstance(x[0], str):
                # http://stackoverflow.com/questions/761804/trimming-a-string-in-python
                desired_subject += x[0].strip()
            else:
                desired_subject += x[0].decode("ascii").strip()
        else:
            desired_subject += x[0].decode(x[1]).strip()
    
    
    return desired_subject
    

# http://stackoverflow.com/questions/1187970/how-to-exit-from-python-without-traceback
def main():
    # src="""
    #     =?UTF-8?B?b3Jn5ris6Kmm5LqM6JmfbWFpbGJveA==?= <s2@skyrock-casting.org>, 
    #     =?UTF-8?B?b3Jn5ris6Kmm5LiA?= <s1@skyrock-casting.org>, 
    #     =?UTF-8?B?5piG5bGx5a+M6YimTWFya+mZsw==?= <mark.chen@fulltech-metal.com>
    #     """
    src="""
        =?UTF-8?B?5Li76aGMIOWwseaYryBTdWJqZXQsIOWcqOa4rOepuueZveeahOWVj+mhjA==?=
        """
    print (mark001_decode(src))
if __name__ == "__main__":
    main()
sys.exit(0)


    
    

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
    
    # bytes to string, 
    raw_message=message.decode("utf-8")
    
    msg =  email.message_from_string(raw_message)
    messageInfo['subject'] = msg['Subject']	    

    headers=Parser().parsestr(message.decode("utf-8"))
    print('To: %s' % headers['to'])
    print('From: %s' % headers['from'])
    print('Subject: %s' % headers['subject'])


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
    
    