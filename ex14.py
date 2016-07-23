from sys import argv

script, user_name, nickname = argv
prompt = 'input here: '

print "Hi %r or %r, I'm the %s script." % (user_name, nickname, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about like me.
You live in %r. Not sure where that is.
And you hava a %r computer. Nice.
""" % (likes, lives, computer)