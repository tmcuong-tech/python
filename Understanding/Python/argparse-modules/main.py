# importing the libraries
import argparse
import sys
import getpass

# correct usnername and password
correct_uname = "admin"
correct_password = "12345"

# instantiate the parser
parser = argparse.ArgumentParser(description='username and password verification')

# adding the arguments
parser.add_argument("-u", "--uname", dest="uname", help="specify the username")
parser.add_argument("-p", "--password", dest="password", nargs="?", help="specify the password")

# parse the arguments
args = parser.parse_args()

if args.password == None:
    args.password = getpass.getpass()

# print arguments
#print(args.uname, args.password)

# username and password verification
if correct_uname == args.uname and correct_password == args.password:
    print("username and password are correct")
else:
    print("username and password are incorrect")

"""
test on terminal
$ python main.py -h
usage: main.py [-h] [-u UNAME] [-p PASSWORD]

username and password verification

optional arguments:
  -h, --help            show this help message and exit
  -u UNAME, --uname UNAME
                        specify the username
  -p PASSWORD, --password PASSWORD
                        specify the password

                        
$ python main.py -u admin -p 1
admin 1
username and password are incorrect


$ python main.py -u admin -p 12345
admin 12345
username and password are correct
"""