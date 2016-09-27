import email
import imaplib
import imaplib_connect
from email.parser import HeaderParser
from imaplib_list_parse import parse_list_response

c = imaplib_connect.open_connection()

c.select()
typ, data = c.search(None, 'ALL')
for num in data[0].split():
    typ, data = c.fetch(num, '(RFC822)')
       
    # print ('Message %s\n%s\n' % (num, data[0][1]))
    print ('Message %s\n' % (num))
    print ('testing %s\n' % (data[0][1]))
    
c.close()
c.logout()
