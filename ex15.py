# input argv variable from sys module
from sys import argv
# set the argv to my variable
script, filename = argv
# open the file which the filename input by argv
txt = open(filename)
# output the message with filename
print "Here's your file %r:" % filename
print txt.read() # output the file's contents
txt.close()
# output message to ask user input a filename
print "Type the filename again:"
file_again = raw_input("> ") # set the input value to my variable
# open the file which the filename input by user
txt_again = open(file_again)
# output the file's contents
print txt_again.read()
txt_again.close()