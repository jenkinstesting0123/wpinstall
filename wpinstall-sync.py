# -*- coding: utf-8 -*-
import mailSender
import MessageTemplate
import Constants
import os
import sys
import getopt
import getpass
from time import gmtime, strftime

MYSQLDUMP_PROCESS = 'mysqldump'
MYSQL_PROCESS = 'mysql56 --force'

SIDIOUS_PARAMS_DUMP = '-u{0} -p{1} -h{2} {3} {4}'


def datadump(user_name, password, host_name, database_name, table_name, file_name):
    try:
        # MessageTemplate.showMessageInConsole('From Sidious process')
        # MessageTemplate.showMessageInConsole('Downloading from SIDIOUS')
        cmd = MYSQLDUMP_PROCESS + ' ' + SIDIOUS_PARAMS_DUMP.format(user_name, password, host_name, database_name, table_name) + ' > ' + file_name
        #cmd = 'mysqldump -u'+user_name+'–p'+password+' -h'+host_name+' '+database_name+' '+table_name+' >'+file_name
        #cmd = 'mysqldump -uadmin -pWelcome123 -hwpinstall.cv8szn5hkhmy.ap-south-1.rds.amazonaws.com wp_install full_usbus >full_usbus.sql'
        os.system(cmd)
        print(cmd)
        # MessageTemplate.NotifyMessage('Succeed', 'From Sidious', 'Data downloaded successfully!', Constants.MAIL_RECIPIENTS_COMPLETE)
    except:
        # MessageTemplate.NotifyMessage('Failed', 'Error From Sidious', sys.exc_info()[0], Constants.MAIL_RECIPIENTS_APP_SUPPORT)
        sys.exit(1)


def dataload(user_name, password, host_name, database_name, file_name):
    try:

        # MessageTemplate.showMessageInConsole('To Sidious process')
        # MessageTemplate.showMessageInConsole('Exporting from CR')
        # cmd = mysql --login-path=data-loader-prdb01 --force --compress --init-command="SET SESSION sql_log_bin=0;" production < full_usbus.sql
        cmd = "mysql -u "+user_name + " –p" + password + " -h" + host_name + \
            " --force --compress --init-command='SET SESSION sql_log_bin=0;'" + \
            database_name + " <"+file_name
        # os.system(cmd)
        #print(cmd)

        # MessageTemplate.NotifyMessage('Succeed', 'To Sidious', 'Data uploaded successfully!', Constants.MAIL_RECIPIENTS_COMPLETE)
    except:
        # MessageTemplate.NotifyMessage('Failed', 'To Sidious', sys.exc_info()[0], Constants.MAIL_RECIPIENTS_APP_SUPPORT)
        sys.exit(1)
        
def validateParams():
    return True

def main(argv):
    user_name = ''
    password = ''
    host_name = ''
    database_name = ''
    table_name = ''
    file_name = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:p:h:d:t:f:g:l:", ['user_name', 'password','host_name' ,'database_name','table_name', 'file_name', 'getdata', 'loaddata'])
    except getopt.GetoptError:
        print('error in arguments')    
    for opt, arg in opts:
        if opt in ('-u' ,'--user_name'):
            user_name=arg
        if opt in ('-p', '--password'):
            password=arg
        if opt in ('-h', '--host_name'):
            host_name=arg
        if opt in ('-d', '--database_name'):
            database_name=arg
        if opt in ('-t', '--table_name'):
            table_name=arg
        if opt in ('-f', '--file_name'):
            file_name=arg
        if opt in ('-g', '--getdata'):
            datadump(user_name, password, host_name, database_name, table_name, file_name)
        if opt in ('-l', '--loaddata'):
            dataload(user_name, password, host_name, database_name, file_name)
if __name__ == '__main__':
    main(sys.argv[1:]) 
