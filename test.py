SIDIOUS_DB_USER = "amir"
SIDIOUS_DB_PWD =  "Welcome"
HOST= "google.com"
DATABASE = "wps"
TABLE = "mytable"

FILENAME = 'amir.sql'

SIDIOUS_PARAMS_DUMP = '-C --skip-secure-auth -u{0} -p{1} '
SIDIOUS_PARAMS_IMPORT = '--skip-secure-auth -u{0} -p{1} -h{2} {3}'

def datadump(user_name, password, host_name, database_name, table_name, file_name):
    #cmd1 = MYSQLDUMP_PROCESS + ' ' + SIDIOUS_PARAMS_DUMP.format(user_name, password, ) + ' > ' + filename
    #cmd2 = "mysqldump -u"+ user_name + " -p" + password + " > " + filename 
    cmd3 = "mysql -u "+user_name+ " –p" +password+ " -h" +host_name+ " --force --compress --init-command='SET SESSION sql_log_bin=0;'"+database_name+ " <"+file_name
   # print(cmd1)
    print(cmd3)

datadump(SIDIOUS_DB_USER, SIDIOUS_DB_PWD, HOST, DATABASE, TABLE, FILENAME)

