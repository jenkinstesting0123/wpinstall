
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def mailSender(title, text, recipients):
	for recipient in recipients:
		sendemail(title, text, recipient)

def sendemail(title, text, pRecipient):
	try:
		sender = 'noreply@neustar.biz'
		recipient = pRecipient

		msg = MIMEMultipart('alternative')
		msg['Subject'] = 'WP CA Notifier: {0}'.format(title)
		msg['From'] = sender
		msg['To'] = recipient

		part = MIMEText(text, 'plain')
		msg.attach(part)

		s = smtplib.SMTP('smartmail.neustar.com')
		s.sendmail(sender, recipient, msg.as_string())
		s.quit()
	except:
		print('Unexpected error: {0}\n\n'.format(sys.exc_info()[0]))