from sys import argv

# take command line args, unpack them
script, input_file = argv

# define a function to read an entire file, outputting it essentially
def print_all(f):
	print f.read()

# define a function to put the file pointer back to beginning
def rewind(f):
	f.seek(0)

# define a functino to print a line count and then read a line from the file
def print_a_line(line_count, f):
	print "Okay",

# open our 2nd command lind arg
current_file = open(input_file)

# calling functions
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
