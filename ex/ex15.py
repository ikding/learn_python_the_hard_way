from sys import argv

script, filename = argv

with open(filename) as txt:
    print "Here's your file %r:" % filename
    print txt.read()

print "Type the file name again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
