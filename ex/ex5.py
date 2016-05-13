name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
bool_var = True

print "Let's talk about %s." % name
print "He's %d inches (%d centimeters) tall." % (height, height*2.54)
print "He's %d pounds (%d kilograms) heavy." % (weight, weight/2.2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print "The boolean variable is: %r" % bool_var
