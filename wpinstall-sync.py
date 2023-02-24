# -*- coding: utf-8 -*-
import mailSender
import MessageTemplate
import Constants
import os
import sys
import getopt
import getpass
from time import gmtime, strftime
import mysql.connector
import subprocess

MYSQLDUMP_PROCESS = 'mysqldump'
MYSQL_PROCESS = 'mysql'
SIDIOUS_PARAMS_DUMP = '-u{0} -p{1} -h{2} {3} {4}'
SIDIOUS_PARAMS_IMPORT = '-u{0} -p{1} -h{2} {3}'

def check_mysql_connectivity(user_name, password, host_name, database_name, port):
    try:
        # Connect to the MySQL database server
        conn = mysql.connector.connect(
        host="host_name",
        database="database_name",
        user="user_name",
        password="password",
        port="port"
    )

        if conn.is_connected():
            print("Connected to MySQL database")

            # Close the communication with the MySQL database server
            conn.close()
            print("Database connection closed")
            return True

    except mysql.connector.Error as error:
        print(f'Failed to connect to MySQL database: {error}')
        return False
    
def validate_file_size(filename, max_size):
    # Check if file exists
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return False

    # Check if file size is less than or equal to max_size
    #
    file_size = os.path.getsize(filename)
    if file_size <= max_size:
        print(f"File '{filename}' size does not have the maximum allowed size of {max_size} bytes.")
        return False

    return True
def dump_mysql_table(host, user, password, db_name, table_name, dump_path):
    try:
        # Construct the mysqldump command
        cmd = ["mysqldump", f"--host={host}", f"--user={user}", f"--password={password}", db_name, table_name]

        # Execute the command and write the output to a file
        with open(dump_path, "w") as dump_file:
            subprocess.run(cmd, stdout=dump_file)

        print(f"Table dump created successfully at {dump_path}")
        # dump_mysql_table(host="localhost", user="root", password="mypassword", db_name="mydatabase", table_name="mytable", dump_path="/path/to/table_dump.sql")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create table dump: {e}")
        sys.exit(1) 


def load_mysql_dump(host, user, password, db_name, dump_path):
    try:
        # Construct the mysql command
        cmd = ["mysql", f"--host={host}", f"--user={user}", f"--password={password}", db_name]

        # Read the dump file and execute it with the mysql command
        with open(dump_path, "rb") as dump_file:
            subprocess.run(cmd, stdin=dump_file)

        print(f"Dump file loaded successfully into database {db_name}")
        #load_mysql_dump(host="localhost", user="root", password="mypassword", db_name="mydatabase", dump_path="/path/to/dump.sql")
    except subprocess.CalledProcessError as e:
        print(f"Failed to load dump file into database {db_name}: {e}")
        sys.exit(1)
 

def datadump(user_name, password, host_name, database_name, table_name, file_name):
    try:
        if check_mysql_connectivity(user_name, password, host_name, database_name, port='3306'):
            # MessageTemplate.showMessageInConsole('From Sidious process')
            # MessageTemplate.showMessageInConsole('Downloading from SIDIOUS')
            dump_mysql_table(host_name, user_name, password, database_name, table_name, file_name)
            #cmd = MYSQLDUMP_PROCESS + ' ' + SIDIOUS_PARAMS_DUMP.format(user_name, password, host_name, database_name, table_name) + ' > ' + file_name
            #os.system(cmd)
            #print(cmd)
            # MessageTemplate.NotifyMessage('Succeed', 'From Sidious', 'Data downloaded successfully!', Constants.MAIL_RECIPIENTS_COMPLETE)
    except:
        # MessageTemplate.NotifyMessage('Failed', 'Error From Sidious', sys.exc_info()[0], Constants.MAIL_RECIPIENTS_APP_SUPPORT)
        sys.exit(1)


def dataload(user_name, password, host_name, database_name, file_name):
    try:
        if check_mysql_connectivity(user_name, password, host_name, database_name, port='3306'):
            if validate_file_size(file_name, 10):
                load_mysql_dump(host_name, user_name, password, database_name, file_name)                                          
                # MessageTemplate.showMessageInConsole('To Sidious process')
                # MessageTemplate.showMessageInConsole('Exporting from CR')
                # cmd = mysql --login-path=data-loader-prdb01 --force --compress --init-command="SET SESSION sql_log_bin=0;" production < full_usbus.sql
                #cmd = MYSQL_PROCESS + ' ' + SIDIOUS_PARAMS_IMPORT.format(user_name, password, host_name, database_name) + ' < ' + file_name
                #os.system(cmd)
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
