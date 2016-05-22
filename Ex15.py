# get argv feature from a package 
from sys import argv
# assigns 1st command line arg to script, 2nd to filename
script, filename = argv
# attempts to open something of that filename in this directory, sets a file to
# be named txt
txt = open(filename)

# prints out what file we just read/opened from command line 
print "Here's your file %r:" % filename
# calls read command on file 
print txt.read()
# closes file
txt.close()

# uses raw_input to get the file name again, and attempt ot open again
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)

# reads it again
print txt_again.read()
txt_again.close()
