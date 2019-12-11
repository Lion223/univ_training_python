# write a function that takes the URL as an argument and returns what is contained at that URL by deleting the HTML markup
from bs4 import BeautifulSoup
import urllib
import nltk
def read_nohtml(url):
    raw_contents = urllib.request.urlopen(url).read()
    return BeautifulSoup(raw_contents, "html.parser").get_text()
text = read_nohtml('http://www.nltk.org/')
text = nltk.word_tokenize(text)
print(text)

# save some text in the corpus.txt file
# define a load (f) function to read a file whose name is its argument and returns a string that contains text from the file
def load(filename):
    text = open(filename).read()
    return text
text = load('corpus.txt')
print(text)

# rewrite the following loop as a list comprehension:
# >>> sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
# >>> result = []
# >>> for word in sent:
# 	... word_len = (word, len (word))
# 	... result.append (word_len)
# >>> result
[('The', 3), ('dog', 3), ('gave', 4), ('John', 4), ('the', 3), ('newspaper', 9)]
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = [(word, len(word)) for word in sent]
print(result)

# check the difference between string and int by doing the following: "3" * 7 and 3 * 7
# try converting using int ("3") and str (3).
print("3" * 7)
print(3 * 7)
string = "3"
integer = 3
print("string to int: ", type(string), int(string), type(int(string)))
print("int to string: ", type(integer), int(integer), type(str(integer)))

# what happens when %6s and %-6s format strings are used to display a string longer than 6 characters?
string = "invincible"
print("%6s" % string)
print("%-6s" % string)

# create a file that will contain the words and their frequency in separate lines across the space (fuzzy 53)
# read this file using open (filename) .readlines ()
# divide each string into two using split (), and convert the number to an integer using int ()
# the result should be in the form of a list: [['' fuzzy ', 53], ...]
file = open('freq.txt').readlines()
res = []
for elem in file:
    spl = elem.split()
    res.append([spl[0], int(spl[1])])
print(res)

# analyze the numerical expression in the following sentence from MedLine: The corresponding free cortisol fractions in these sera were 4.53 +/- 0.15% and 8.16 +/- 0.23%, respectively
# can you say that 4.53 +/- 0.15% is three separate words? 
# is this one compound word? Is it nine words "four point five three, plus or minus fifteen percent"? 
# isn't that a word at all? When solving which tasks should one or another answer be chosen?

# according to the analysis, the best options for segmentation are those whose value of the objective function is 161
# however, the first word suggests that segmentation of this sentence requires more information
# ”Four point five three, plus or minus fifteen percent” - nine words, although the analysis of "plusorminuszero" is one word
# the difference arises when performing tasks related to speech processing, including mathematical tasks
from random import randint
text = "The corresponding free cortisol fractions in these sera were 4.53 +/- 0.15% and 8.16 +/- 0.23%, respectively."
start = "Thecorrespondingfreecortisolfractionsintheseserawerefourpointfiftythreeplusorminuszeropointfifteenpercentandeightpointsixteenplusorminuszeropointtwentythreepercentrespectively"
seg1 =  "001000000000000100010000000100000000101000010001000100010000100001000010001010000100010000100000010000001001000010000100000010001010000100010000100000100001000000100000000000"
seg0 =  "000000000000000100000000000100000000000000010000000100010000100001000010000010000100010000100000010000000001000010000100000010000000000100010000100000100001000000100000000000"
def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words

def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size

def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0,len(segs)-1))
    return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature)))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    print
    print(segs)
anneal(start, seg0, 5000, 1.2)

# measure of readability is used to evaluate the complexity of a text to read
# suppose that μw is the average number of letters in a word, and μs is the average number of words in a sentence in a given text
# the Automated Readability Index (ARI) of the text is determined by the expression: 4.71 μw + 0.5 μs - 21.43
# determine ARI values for different parts of Brown Corpus, including part f (popular lore) and j (learned)
# use nltk.corpus.brown.words () to find the word sequence and nltk.corpus.brown.sents () to find the sequence of sentences
from nltk.corpus import brown
from prettytable import PrettyTable

def calcARI(category):
    avg_words = 0
    avg_letters = 0
    for sentence in brown.sents(categories=category):
        avg_words += len(sentence)
    avg_words = avg_words / len(brown.sents(categories=category))
    for word in brown.words(categories=category):
        avg_letters += len(word)
    avg_letters = avg_letters / len(brown.words(categories=category))
    return (4.71 * avg_letters) + (0.5 * avg_words) - 21.43

x = PrettyTable(["Genres", "ARI"])
for c in brown.categories():
    x.add_row([c, calcARI(c)])
print(x)

# access ABC Rural News and ABC Science News Corps texts (nltk.corpus.abc)
# find a value for evaluating the readability of texts (similar to task # 12)
# use Punkt to separate text into individual sentences

# The difference in ARI value from the previous exercise is explained by Punkt's work in dividing the text into sentences, resulting in the sentence being too large
from nltk.corpus import abc
import nltk
from prettytable import PrettyTable

def calcARI(file):
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    text = abc.raw(file)
    sents = sent_tokenizer.tokenize(text)
    avg_words = 0
    avg_letters = 0
    for sentence in sents:
        avg_words += len(sentence)
    avg_words = avg_words / len(sents)
    for word in abc.words(file):
        avg_letters += len(word)
    avg_letters = avg_letters / len(abc.words(file))
    return (4.71 * avg_letters) + (0.5 * avg_words) - 21.43

x = PrettyTable(["File", "ARI"])
for f in abc.fileids():
    x.add_row([f, calcARI(f)])
print(x)