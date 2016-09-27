import imaplib
import imaplib_connect

c = imaplib_connect.open_connection()
try:
    typ, data = c.select('INBOX')
    print (typ, data)
    num_msgs = int(data[0])
    print ('There are %d messages in INBOX' % num_msgs)
finally:
    c.close()
    c.logout()