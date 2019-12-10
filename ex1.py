# perform arithmetic operations with string
msg = 'Firstname Lastname'
print((msg + '\n')* 3)

# using slices, remove affixes in the following wordforms: dish-es, run-ning, nation-ality, un-do, pre-heat
affixes = ['dishes', 'running', 'nationality', 'undo', 'preheat']
dishes = affixes[0][0:4]
running = affixes[1][0:3]
nationality = affixes[2][0:6]
undo = affixes[3][0:2]
preheat = affixes[4][0:3]
print(dishes + ' ' + running + ' ' + nationality + ' ' + undo + ' ' + preheat)

# explain the result of executing msg [:: - 1]

# the slice [:: - 1] contains three arguments - two colon and "-1"
# the first two arguments return a slice containing the entire string because the boundaries are undefined
# the last argument defines the step, so the slice returns the inverted string
print(dishes[::-1])

# provide last name, first name and patronymic as a list of tapes
# use the .reverse () method and slice [:: - 1] to change the string. Explain the results

# the .reverse () method returns the name in the reverse order
# the slice [:: - 1] returns a reverse string according to previous exercise
name = ['Lastname', 'Firstname', 'Middlename']
name.reverse()
print(name[0][::-1])

# create a test.py file containing the msg string
# use the following statements and explain the results
# >>> from test import msg
# >>> msg

# The first code line loads an element (msg string) from the test module
from test import msg
print(msg)

# write a program that converts a list of strings into one string
print(''.join(name))

# write a program that prints words from the string silly in alphabetical order
silly = 'some randomly choosed words and...'
words = silly.split()
words.sort()
for word in words:
    print(word)

