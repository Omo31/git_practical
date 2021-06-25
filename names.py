import os

 #code for local file path on screen
print(os .getcwd())
print('\n''\n')


# The text file assignment with my full name
names = open('mynames.txt', 'w+')
names.writelines(['Firstname: Omowumi', '\nMiddlename: Olabisi', '\nLastname: Badmus'])
names.close()


with open('mynames.txt', 'r') as names:
    for name in names:

        print(name)



import linecache

fname = linecache.getline('mynames.txt', 1)
print('\n''\n')
print(fname)

mname = linecache.getline('mynames.txt', 2)
print('\n''\n')
print(mname)

lname = linecache.getline('mynames.txt', 3)
print('\n''\n')
print(lname)


