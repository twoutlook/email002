import base64
import email
import imaplib
import imaplib_connect
from email.parser import HeaderParser
from imaplib_list_parse import parse_list_response
from email.header import decode_header

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from smtplib import SMTP
# https://docs.python.org/3/library/email.header.html
# https://docs.python.org/3/library/email-examples.html

# http://stackoverflow.com/questions/3401428/how-to-get-an-isoformat-datetime-string-including-the-default-timezone
import datetime, pytz
# datetime.datetime.now(pytz.timezone('US/Central')).isoformat()

'''
Mail Server Username: s2@skyrock-casting.org

Standard (without SSL)
Incoming Mail Server: mail.skyrock-casting.org
Supported Ports: 143 (IMAP), 110 (POP3)
Outgoing Mail Server: mail.skyrock-casting.org
Supported Port: 26 (server requires authentication)

Private (with SSL)
Incoming Mail Server: host411.hostmonster.com (SSL)
Supported Ports: 993 (IMAP), 995 (POP3)
Outgoing Mail Server: host411.hostmonster.com (SSL)
Supported Port: 465 (server requires authentication)

Supported Incoming Mail Protocols: POP3, IMAP
Supported Outgoing Mail Protocols: SMTP 
'''


def send_testing_email():
    me = "s2@skyrock-casting.org"
    # you = ["s1@skyrock-casting.org,chenpingling@protonmail.com, chenpingling@gmail.com"]
    #you = "chenpingling@protonmail.com, chenpingling@gmail.com"
    # you = "chenpingling@gmail.com"
    you = ["mark.chen@fulltech-metal.com" ,"mark.chen@skyrock-casting.com","s1@skyrock-casting.org","chenpingling@protonmail.com", "chenpingling@gmail.com"]
    #
    print (me, you)
  
    # dtstr=datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    dtstr=datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%m/%d %H:%M:%S')
    print (dtstr)
  
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = dtstr+" 使用 Python 程式直接發信 yyy multiple recipients "
    msg['From'] = me
    
    # http://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
    # msg['To'] = = ", ".join(recipients)
    msg['To'] = ", ".join(you)
    
    # msg['To'] = ["s1@skyrock-casting.org,chenpingling@protonmail.com, chenpingling@gmail.com"]
    # msg['To'] = ["s1@skyrock-casting.org,chenpingling@protonmail.com, chenpingling@gmail.com"]
    
    # Create the body of the message (a plain-text and an HTML version).
    text = "所以發信者是要準備兩種格式? Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Here is the <a href="https://www.python.org">link</a> you wanted.
        </p>
      </body>
    </html>
    """
    print (msg)
  
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    
    # Send the message via local SMTP server.
    # s = smtplib.SMTP('localhost')
    # s = smtplib.SMTP()
    # http://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp
    conn = SMTP('mail.skyrock-casting.org',"26")
    
    conn.login('s2@skyrock-casting.org',"Kunshan@2016")
    
    
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    
    try:
        # print ("DEBUG ONLY, NOT SENDING THIS EMAIL")
   
        conn.sendmail(me, you, msg.as_string())
        print ("conn.sendmail, done!")
   
    finally:
        conn.quit()

send_testing_email()





# def check_subjects():
#     M = imaplib_connect.open_connection()
    
#     M.select()
#     typ, data = M.search(None, 'ALL')
    
#     messages = []
#     messageInfo = {}
    
#     # http://www.tutorialspoint.com/python/string_find.htm
    
    
    
#     for num in data[0].split():
#         typ, data = M.fetch(num, '(RFC822)')
        
#         message = data[0][1]
        
#         # bytes to string, 
#         raw_message=message.decode("utf-8")
        
#         msg =  email.message_from_string(raw_message)
#         messageInfo['subject'] = msg['Subject']	    
    
#         to_decode = decode_header( messageInfo['subject'] )
#         desired_subject=""
#         for x in to_decode:
#             # print(    "    ",x)
#             # print( "    ---",x[0])
#             # print( "    coding:",x[1])
#             if (x[1] == None):
#                 # WHY, 有時候是bytes, 有時候是string? 
#                 if isinstance(x[0], str):
#                     desired_subject += x[0]
#                 else:
#                     desired_subject += x[0].decode("ascii")
#             else:
#                 desired_subject += x[0].decode(x[1])
#             print(num.decode("ascii"),desired_subject)

# check_subjects()
    