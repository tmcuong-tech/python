# importing the libraries
import sys
import getopt

# taking all the argument except filename
argv = sys.argv[1:]

# correect username and password
correvt_name = "admin"
correct_password = "123456"

# write a try catch block
try:
    # colon means a value is expected
    opts, args = getopt.getopt(argv, "u:p:", ["uname=", "password="])

    print(opts, args)

    if len(opts) != 2:
        print("usage: cmd_getopt_tutorial -u <uname> -p <password> or")
        print("usage: cmd_getopt_tutorial --uname <uname> --password <password>")

    # we need the values for uname and password witch we typed on the command line
    for opt, arg in opts:
        if opt == '-u' or opt == '--uname':
            uname = arg
        elif opt == '-p' or opt == "--password":
            password = arg

    # username and password verification
    if uname == correct_password and password == correct_password:
        print("username and password are correct")
    else:
        print("username and password are incorrect")

except getopt.GetoptError: # if any option is not reognized
    print("one or more option(s) art not recognize or not in conrrect format")

"""
test on terminal
$ python main.py -u admin -p 123456
[('-u', 'admin'), ('-p', '123456')] []
username and password are incorrect

$ python main.py -u haha -p 123
[('-u', 'haha'), ('-p', '123')] []
username and password are incorrect
"""