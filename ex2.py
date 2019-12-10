# create a variable sentence and assign it a value of 'she sells sea shells by the sea shore' and write a snippet 
# that generates a new string by adding 'like' before each word that begins with 'se'
import re
sentence = 'she sells sea shells by the sea shore'
sentence = re.split("( )",sentence)
new_sentence = ''
for word in sentence:
    if word.startswith('se'):
        word = 'like ' + word
    new_sentence += word
print(new_sentence)

# empty string and empty list in the if statement causes an error
# write the program to demonstrate that case
string = ""
list = []
try:
    if list[0] in string[1]:
        print('cool')
except IndexError:
    print('index out of bounds exception')

# follow the examples below and explain the difference

# the difference is that the isupper () method returns true only when all of the string characters are uppercase 
# the "not w.islower ()" condition returns true only when the all characters in the string are non-uppercase
# thus, in this example, the second condition is satisfied because the digits are not case sensitive
w = '12'
if w.isupper():
    print('w contains only upper letters')
elif not w.islower():
    print('w contains only upper or/and case-unsupported characters(digits)')

# find in text #5 all words that are 4 in length and build a frequency distribution for them
from nltk.book import *
from nltk.probability import FreqDist
list = []
for w in text5:
    if len(w) == 4:
        list.append(w)
fdist = FreqDist(list)
fdist.plot(10, cumulative=True)
    
# use the expression sum ([len (w) for w in text1]) to find the average length of words in the text
from nltk.book import *
words = [w for w in text1]
avg = sum([len(w) for w in text1]) / len(words)
print('Avg length of words in the text1: %f' % (avg))

# build collocations for texts #1 and #6
from nltk.book import *
from nltk.collocations import BigramCollocationFinder 
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords 

    # engl stopwords
stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset 
text1_words = [w.lower() for w in text1]
    # text1 colloc
biagram_collocation_text1 = BigramCollocationFinder.from_words(text1_words)
biagram_collocation_text1.apply_word_filter(filter_stops)
print('Text1 collocation (top-15 bigrams):\n')
print(biagram_collocation_text1.nbest(BigramAssocMeasures.raw_freq, 15))
text6_words = [w.lower() for w in text6]
    # text6 colloc
biagram_collocation_text6 = BigramCollocationFinder.from_words(text6_words)
biagram_collocation_text6.apply_word_filter(filter_stops)
print('Text6 collocation (top-15 bigrams):\n')
print(biagram_collocation_text6.nbest(BigramAssocMeasures.raw_freq, 15))
