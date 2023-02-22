
import mailSender
from time import gmtime, strftime

def showMessageInConsole(message):
    print ('### Doing: {0} at: {1} ###\n\n'.format(message, strftime("%Y-%m-%d_%H:%M:%S", gmtime())))

def NotifyMessage(action, title, description, mailList):
    mailSender.mailSender(title, description, mailList)
    print('{2} on {0}: {1}\n\n'.format(title, description, action))