import os

print(os.getcwd()) # D:\python\os-modules --> return current position <=> pwd

#os.rename("first.txt", "second.txt") # reanme file with os.rename("old_name_file","new_name_file")

os.system('ls') # retturn list files in current directory <=> ls

print("your current working directory is: " + os.getcwd() + "\n\n")
print("the conents of this directory are: ")
print(os.system('ls'))

file = input("enter a file name: ")
if os.path.isfile(file):
    print("the file exists") # return this line if in your current directory has that file
else:
    print("the file does not exist") # return this line if in your current directory has not that file
    print("creatring it...")
    os.system(f'touch {file}')