# -*- coding: utf-8 -*-
import mailSender
import MessageTemplate
import Constants
import os
import sys, getopt, getpass
from time import gmtime, strftime

def datadump(user_name, password, host_name, database_name, table_name, file_name):
    try:
        MessageTemplate.showMessageInConsole('From Sidious process')
        MessageTemplate.showMessageInConsole('Downloading from SIDIOUS')
        #cmd = mysqldump --login-path=dev-sidious --force production full_usbus > full_usbus.sql
        cmd = "mysqldump -u "+user_name+ " –p" +password+ " -h" +host_name+ " " +database_name+ " "+table_name+ " >" +file_name
        #os.system(cmd)
        #MessageTemplate.NotifyMessage('Succeed', 'From Sidious', 'Data downloaded successfully!', Constants.MAIL_RECIPIENTS_COMPLETE)
    except:
        #MessageTemplate.NotifyMessage('Failed', 'Error From Sidious', sys.exc_info()[0], Constants.MAIL_RECIPIENTS_APP_SUPPORT)
        sys.exit(1)


def dataload(user_name, password, host_name, database_name, file_name):
    try:
        
        #MessageTemplate.showMessageInConsole('To Sidious process')
        #MessageTemplate.showMessageInConsole('Exporting from CR')
        #cmd = mysql --login-path=data-loader-prdb01 --force --compress --init-command="SET SESSION sql_log_bin=0;" production < full_usbus.sql
        cmd = "mysql -u "+user_name+ " –p" +password+ " -h" +host_name+ " --force --compress --init-command='SET SESSION sql_log_bin=0;'"+database_name+ " <"+file_name      
        #os.system(cmd)
	#print(cmd.decode('utf-8'))
		
        #MessageTemplate.NotifyMessage('Succeed', 'To Sidious', 'Data uploaded successfully!', Constants.MAIL_RECIPIENTS_COMPLETE)
    except:
        #MessageTemplate.NotifyMessage('Failed', 'To Sidious', sys.exc_info()[0], Constants.MAIL_RECIPIENTS_APP_SUPPORT)
        sys.exit(1)



def validateParams():
   """ try:
        if len(sys.argv) != 4:
            raise
    except:
        print('Must be typed one parameter')
        return False
    try:
        if not isinstance(sys.argv[1], str):
            raise
    except:
        print('Entered param must be string')
        return False """
   return True


def main(argv):
    user_name=''
    password='' 
    host_name='' 
    database_name=''
    table_name=''
    file_name =''
    
    if validateParams():
        try:
          opts, args = getopt.getopt(sys.argv[1:], 'dluphdtf:', ['dumpdata', 'loaddata','user_name','password','host_name','database_name','table_name','file_name'])
        except getopt.GetoptError:
            print('error in arguments')
        for opt, arg in opts:
            #MessageTemplate.showMessageInConsole('opt: {0} - arg: {1}'.format(opt, arg))
            if opt in ('-u', '--user_name'):
                print(arg)
            elif opt in ('-p', '--password'):
                password = arg
            elif opt in ('-h', '--host_name'):
                host_name=arg
            elif opt in ('-d', '--database_name'):
                databae_name=arg
            elif opt in ('-t', '--table_name'):
                table_name=arg               
            elif opt in ('-f', '--file_name'):
                file_name=arg
            elif opt in ('-d', '--dumpdata'):
                datadump(user_name, password, host_name, database_name, table_name, file_name)              
            elif opt in ('-l', '--loaddata'):
                dataload(user_name, password, host_name, database_name, file_name)
    else:
        #MessageTemplate.NotifyMessage('Failed', 'In Main', sys.exc_info()[0], Constants.MAIL_RECIPIENTS_APP_SUPPORT)
        print('Invalid parameters entered')
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
