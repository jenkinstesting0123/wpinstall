import sys
import getopt
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
            print(user_name)
            print(password)
            print(host_name)
            print(database_name)
            print(table_name)
            print(file_name)
            print('gettingdata=========')
        if opt in ('-l', '--loaddata'):
            print(user_name)
            print(password)
            print(host_name)
            print(database_name)
            print(table_name)
            print(file_name)
if __name__ == '__main__':
    main(sys.argv[1:]) 