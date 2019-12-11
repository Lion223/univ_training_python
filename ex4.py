# use a comparative dictionary to find close words for German, Italian and English
from nltk.corpus import swadesh
from nltk.corpus import wordnet as wn
lang = ['en', 'de', 'it']
synonyms = []
print('Word: ' + str(swadesh.entries(lang)[182]))
for s in wn.synsets(swadesh.entries(lang)[182][0]):
    for l in s.lemmas():
        synonyms.append(l.name())
synonyms = list(set(synonyms))
print('Synonyms: ', synonyms)
print('Translation: ')
for s in synonyms:
    try:
        print('%s (german): %s' % (s, dict(swadesh.entries(['en', 'de']))[s]))
        print('%s (italian): %s' % (s, dict(swadesh.entries(['en', 'it']))[s]))
    except:
        pass

# construct a conditional frequency distribution for the corpus of names
# find out which first letters are more commonly used in both masculine and feminine names
import nltk.corpus
names = nltk.corpus.names
male = []
female = []
for name in names.words('male.txt'):
    male.append(name[0])
for name in names.words('female.txt'):
    female.append(name[0])
def most_frequent(List): 
    return max(set(List), key = List.count)
ff = most_frequent(female)
fm = most_frequent(male)
print('Most frequent first symbol of female names: ', ff +
      ' (' + str(female.count(ff)) + ')')
print('Most frequent first symbol of male names: ', fm +
      ' (' + str(male.count(fm)) + ')')
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()

# analyze the pronunciation dictionary
# find how many different words it contains
# what percentage of the words in this dictionary can have different pronunciation?
import nltk.corpus
entries = nltk.corpus.cmudict.entries()
words = []
dif_words = []
for w in entries:
    words.append(w[0])
dif_words = list(set(words))
dif = (1 - len(dif_words)/len(words)) * 100
print("Diff words count: ", len(dif_words))
print("Percentage of words with different pronunciation: ", str(dif) + '%')

# modify a random text generation program to do the following: train the program on texts of different genres and different corpora
# generate text with 5 different starting words
import nltk
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        
t1 = nltk.corpus.brown.words(categories='news')
bigrams1 = nltk.bigrams(t1)
cfd = nltk.ConditionalFreqDist(bigrams1)
print(generate_model(cfd, 'today'))

t2 = nltk.corpus.gutenberg.words('blake-poems.txt')
bigrams2 = nltk.bigrams(t2)
cfd = nltk.ConditionalFreqDist(bigrams2)
print(generate_model(cfd, 'down'))

t3 = nltk.corpus.reuters.words(categories='coffee')
bigrams3 = nltk.bigrams(t3)
cfd = nltk.ConditionalFreqDist(bigrams3)
print(generate_model(cfd, 'coffee'))

t4 = nltk.corpus.comparative_sentences.words()
bigrams4 = nltk.bigrams(t4)
cfd = nltk.ConditionalFreqDist(bigrams4)
print(generate_model(cfd, 'work'))

t5 = nltk.corpus.brown.words(categories='lore')
bigrams5 = nltk.bigrams(t5)
cfd = nltk.ConditionalFreqDist(bigrams5)
print(generate_model(cfd, 'good'))

# find the average value of polysemy for adverbs
from nltk.corpus import wordnet as wn
import re
print("Enter a sentence with adverbs:")
string = input()
adv = re.findall(r"\b\w+ly\b", string)
random = 1000
print("Adverbs:")
print(adv)
print("Polysemes:")
i = 0
for w in adv:
    i += len(wn.synsets(w, 'r'))
    print(wn.synsets(w, 'r'))
print("Adverb count: ", len(adv))
print("Polysemes: ", i)
print("Avg: ", str(i/len(adv)))

print("\n\nSample of" + str(random) + " words - ")
words = []
for synset in list(wn.all_synsets('r'))[:1000]:
    for word in synset.lemma_names():
        words.append(word)
words = [w for w in words if w[-2:] in 'ly']
print("Adverb count: ", len(set(words)))
print("Polysemes: ", len(words))
print("Avg: ", str(len(words)/len(set(words))))

# using one of the word similarity methods, build a descending list of similarity values for the following word pairs: 
# monk-oracle, cemetery-woodland, food-rooster, coast-hill, forest-graveyard, crane-implement, journey-car, coast -shore, 
# asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock
from nltk.corpus import wordnet as wn
pairs = [('monk', 'oracle'), ('cemetery', 'woodland'), ('food', 'rooster'),
         ('coast', 'hill'), ('forest', 'graveyard'), ('crane', 'implement'),
         ('journey', 'car'), ('coast', 'shore'), ('asylum', 'madhouse'),
         ('magician', 'wizard'), ('midday', 'noon'), ('furnace', 'stove'),
         ('food', 'fruit'), ('bird', 'cock')]
def takeThird(elem):
    return elem[2]
results = []
for i in pairs:
    first = wn.synsets(i[0])[0]
    second = wn.synsets(i[1])[0]
    i += first.path_similarity(second),
    results.append(i)
results.sort(key=takeThird, reverse=True)
for e in results:
    print(e)