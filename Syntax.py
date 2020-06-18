#Multi-line Strings
#Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. 
# Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one, 
# we tell the program that the string doesn’t end until the next triple-quote. 
# This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.

# Assign the string here
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""


print(to_you)

