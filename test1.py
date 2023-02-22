
import getopt, sys


def validateParams():

    return True


def main(argv):
    user_name = ''
    password = ''
    if validateParams():
        try:
            opts, args = getopt.getopt(argv, 'hftup:', ['from_sidious', 'to_sidious', 'user_name' 'password='])
            print(opts)
        except getopt.GetoptError:
            print('Synchronizer.py -f or --from_sidious, -t or --to_sidious, -b or --backup_on_sidious, -u or --update_WPCA')
            sys.exit(2)
        for opt, arg in opts:
            #print('opt: {0} - arg: {1}'.format(opt, arg))
            if opt == '-h':
                print('Synchronizer.py -f or --from_sidious, -t or --to_sidious, -b or --backup_on_sidious, -u or --update_WPCA')
            elif opt in ('-u', '--user_name'):
                user_name = arg
            elif opt in ('-p', '--password'):
                password = arg
            elif opt in ('-f', '--from_sidious'):
                print("")
            elif opt in ('-t', '--to_sidious'):
                print("uploading data with ")
    else:
        #MessageTemplate.NotifyMessage('Failed', 'In Main', sys.exc_info()[0], Constants.MAIL_RECIPIENTS_APP_SUPPORT)
        print('Invalid parameters entered')
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])

