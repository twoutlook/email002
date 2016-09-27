# http://imapclient.readthedocs.io/en/stable/


# https://my.hostmonster.com/cgi/email_manager/config
# s1@skyrock-casting.org
# Kunshan@2016

from __future__ import unicode_literals

from imapclient import IMAPClient

HOST = 'mail.skyrock-casting.org'
USERNAME = 's1@skyrock-casting.org'
PASSWORD = 'Kunshan@2016'
ssl = False

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

select_info = server.select_folder('INBOX')
# print('%d messages in INBOX' % select_info['EXISTS'])

print("select_info...")
print(select_info)

messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted" % len(messages))

print()
print("Messages:")
response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE'])

print("response")
print(response)


# for msgid, data in response.iteritems():
#     print('   ID %d: %d bytes, flags=%s' % (msgid,
#                                             data[b'RFC822.SIZE'],
#                                             data[b'FLAGS']))for msgid, data in response.iteritems():
# for msgid, data in response.iteritems():
#     print('   ID %d: %d bytes, flags=%s' % (msgid,
#                                             data[b'RFC822.SIZE'],
#                                             data[b'FLAGS']))