import sys,traceback
import getopt

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
def main(argv):
    # src="""
    #     =?UTF-8?B?b3Jn5ris6Kmm5LqM6JmfbWFpbGJveA==?= <s2@skyrock-casting.org>, 
    #     =?UTF-8?B?b3Jn5ris6Kmm5LiA?= <s1@skyrock-casting.org>, 
    #     =?UTF-8?B?5piG5bGx5a+M6YimTWFya+mZsw==?= <mark.chen@fulltech-metal.com>
    #     """
    src="""
        =?UTF-8?B?5Li76aGMIOWwseaYryBTdWJqZXQsIOWcqOa4rOepuueZveeahOWVj+mhjA==?=
        """
    print (mark001_decode(src))
    print (argv)
    
    
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm
if __name__ == "__main__":
    main(sys.argv[1])
