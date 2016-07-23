name = 'Deron Lee'
age = 36 # not a lie
height = 183 # cms
height_inches = 183 / 2.54 

weight = 95 #kgs
weight_pounds = 95 * 2.20462

eyes = 'Blue' # I wish lol
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d cms or %r inches tall." % (height, height_inches)
print "He's %d kgs or %d lbs heavy." % (weight, weight_pounds)
print "Actually that's not too heary."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)