# define a function to print out the amount of cheeses and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# give the number directly to the function	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# give the number to variable and send them to function
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# give the number in math 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# give the variable to math
print "And we can combine the two, ariables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def how_old_are_you(age):
	print "you are %d old" % age
	
my_age = 35
my_age_ten_years_ago = 25
my_wife_age = 34
age_older_than_my_wife = 1	
how_old_are_you(35)
how_old_are_you(18+17)
how_old_are_you(my_age)
how_old_are_you(my_wife_age + 1)
how_old_are_you(my_wife_age + age_older_than_my_wife)
how_old_are_you(my_age_ten_years_ago + 10)
