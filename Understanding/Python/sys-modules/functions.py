import sys


print(sys.platform) # win32
print(sys.copyright)
"""
# output:
Copyright (c) 2001-2024 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
"""

print(sys.version)
# output: 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)]

sys.stdout.write("Hello friend!\n") # Hello friend!
sys.stderr.write("fsociety\n") # fsociety

a = 15
b = 12.78
c = 'hello'
d = ['list', 123, 123.123]


print(sys.getsizeof(a)) # 28
print(sys.getsizeof(b)) # 24
print(sys.getsizeof(c)) # 46
print(sys.getsizeof(d)) # 88


#print(sys.argv)
"""
first: create virtual enviroment

for windows
command to create: python -m venv venv
command to activate (for terminal): .\venv\Stripts\Activate.bat
ommand to activate (for powershell): .venv\Scripts\Activate

for linux
command to create: python -m venv venv
command to activate: source venv/bin/activate
                or: ./venv/bin/activate

on terminal:
input:
python <file_name> arg1, arg2, ...

output:
['arg1', 'arg2', ...]
"""

l = sys.argv
print("hello", l[1], "you are", l[2], "years old and you are", l[3])