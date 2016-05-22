hairs = ['brown', 'blonde', 'red']
eyes = ['yellow', 'sludge', 'boogers']
weights = [1,2,3,4]
mixed = [1,  "yes", 3, "Okay"]

for number in weights:
	print "This is the number %d" % number

for hair in hairs:
	print "A hair of type : %s" % hair

for i in mixed:
	print "I got %r:" % i

# we can also build lists, first start with an empty one
elements = []

for i in range(0,6):
	print "Adding %d to the list." % i
	# lists understand append
	elements.append(i)

for i in elements:
	print "Element was %d" % i

print elements
del elements[1]
print elements

twoArray = [[1,2,3],[4,5,6]]
print twoArray



