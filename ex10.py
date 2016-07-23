tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print "%s" % fat_cat

print "I do those: 1\\1 2\a2 3\b3 4\f4 5\r\5 6\v6 7\ooo7"

while True:
	for i in [ "-", "/", "|", "\\", "-"]:
		print "%s\r" % i,