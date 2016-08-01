def make_a_list(number, increment):
	i = 0
	numbers = []

	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	

	print "The numbers: "

	for num in numbers:
		print num
		
def make_a_list_for(number, increment):
	numbers = []

	for i in range(0, number, increment):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	

	print "The numbers: "

	for num in numbers:
		print num
	
make_a_list(8, 2)	
make_a_list_for(8, 2)
