from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

moreInput = raw_input("I'll take more:")
print "Here's your more %r" % moreInput
