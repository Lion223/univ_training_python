# read texts from the State of the Union addresses using the state_union module
# determine the frequency of use of the words "men", "women", "people" in each document 
import nltk
from nltk.corpus import state_union

state_files = state_union.fileids()
words = ['men', 'women', 'people']

cfd = nltk.ConditionalFreqDist(
    (text, word)
    for text in state_files
    for word in state_union.words(text))
cfd.tabulate(conditions=state_files, samples=words)

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_files
    for word in state_union.words(fileid)
    for target in words
    if word.lower().startswith(target))
cfd.plot()

# analyze the frequency chart of modal verbs for different genres
# find other word use classes that also differ in different genres
import nltk
import nltk.corpus
corpus_name = nltk.corpus.brown
files = corpus_name.fileids()
modals = ['can', 'could', 'may', 'might', 'must', 'will']
commons = ['the', 'be', 'to', 'of', 'and', 'in', 'that']
adjectives = ['good', 'new', 'first', 'last', 'long']
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in corpus_name.categories()
    for word in corpus_name.words(categories=genre))
cfd.tabulate(conditions=genres, samples=modals)
print()
cfd.tabulate(conditions=genres, samples=commons)
print()
cfd.tabulate(conditions=genres, samples=adjectives)

# write a program to find all words in the Brown case that occur at least three times
import nltk
import nltk.corpus
corpus_name = nltk.corpus.brown
words = corpus_name.words()
fdist = nltk.FreqDist(w.lower() for w in words)
min_occur = 3
filtered_list = list(filter(lambda x: x[1]>=min_occur,fdist.items()))
print(sorted(filtered_list, key=lambda tup: tup[1], reverse=True)[:10])

# write a program that generates table word / original word ratio for all genres of Brown
import nltk
import nltk.corpus
from prettytable import PrettyTable
corpus_name = nltk.corpus.brown
files = corpus_name.fileids()
x = PrettyTable(["Genres", "All", "Original", "O/A"])
for genre in corpus_name.categories():
    words = len(corpus_name.words(categories=genre))
    words_original = len(set(corpus_name.words(categories=genre)))
    x.add_row([genre, words, words_original, float(words_original/words)])
print(x)

# write a program to create a word frequency table for different genres
# find words whose presence or absence is characteristic for certain genres (similar to modal verbs)
import nltk
import nltk.corpus
corpus_name = nltk.corpus.brown
files = corpus_name.fileids()
prepositions = ['under', 'between', 'over', 'on', 'after', 'by', 'without']
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in corpus_name.categories()
    for word in corpus_name.words(categories=genre))
cfd.tabulate(conditions=genres, samples=prepositions)

# identify a hedge (text) function that processes text and creates a new version of that text by adding the word 'like' before every third word
some_text = 'Hello, my name does not matter, but still i can be of some help'
def hedge(text):
    process = []
    result = ''
    words = text.split()
    i = 1
    for w in words:
        if i % 3 == 0:
            process.append('like ' + w)
        else:
            process.append(w)
        i += 1
    for w in process:
        result += w + ' '
    return result
print(hedge(some_text))