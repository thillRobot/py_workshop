# Intro to Programming with Python - ENGR1220 - GSET
# Tristan Hiil - Lecture 5 - Strings - June 11, 2023 

# using strings in python - example 1
string1='Single quotes are nice!'
string2="Double quotes allow 'embedded' single quotes" 
string3='''Triple quote (single or double) allow for
multiple line strings (and need to be tested)'''
print(string1)
print(string2)
print(string3)

# using strings in python example 2 
language='Python 3'

print('The string is:', language) 
print('The first item is:', language[0])
print('The last item is:', language[len(language)-1])

#using strings in python example 3 (continued)
language='Python 3'
# language[7]='2' # uncomment to see immutability error

# common sequence operators (not exhaustive list)

# in - used for logical tests
print('P' in language)
print('Q' in language)
print('R' not in language)

# slice - index a section 
center_slice=language[1:4]
more_stuff='is not a word'
# concatenation - add parts
print(center_slice + more_stuff)

separated_stuff=more_stuff.split(' ')
print(separated_stuff, "now has", len(separated_stuff), "items") 


