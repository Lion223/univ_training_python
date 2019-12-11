# describe which string classes correspond to the following regular expression. [a-zA-Z]+. Check results using nltk.re_show ()

# string classes: A character in the range of "a" to "z" or "A" to "Z" with one repetition or more
import nltk, re
words = ['hello', 'John', 'random', 'INSANITY', 'guess', 'name', 'true', 'please', 'underestimated', '12', 'test!']
string = 'hello John random INSANITY guess name true please underestimated 12 test!'
reg = '[a-zA-Z]+'
print([w for w in words if re.search(reg, w)])
print(nltk.re_show(reg, string))

# describe which string classes correspond to the following regular expression. [A-Z][a-z] *. Check results using nltk.re_show ()

# string classes: A character in the range of “A” to “Z” and a character in the range of “a” to “z” without or more repetitions
import nltk, re
words = ['hello', 'John', 'random', 'INSANITY', 'guess', 'name', 'true', 'please', 'underestimated', '12', 'test!']
string = 'hello John random INSANITY guess name true please underestimated 12 test!'
reg = '^[A-Z][a-z]*$'
print([w for w in words if re.search(reg, w)])
print(nltk.re_show(reg, string))

# describe which string classes correspond to the following regular expression. \d+(\.\d+). Check results using nltk.re_show ()

# string classes: any number with one repetition or more and an optional group containing the character "." And any number with one repetition or more
import nltk, re
words = ['hello', '3.354', 'John', 'random', 'INSANITY', 'guess', 'name', 'true', 'please', 'underestimated', '12', 'test!']
string = 'hello 3.354 John random INSANITY guess name true please underestimated 12 test!'
reg = r'\d+(\.\d+)?'
print([w for w in words if re.search(reg, w)])
print(nltk.re_show(reg, string))

# describe which string classes correspond to the following regular expression. ([^aeiou][aeiou][^aeiou])*. Check results using nltk.re_show ()

# string classes: a group with no or more repetitions, in which the first character is not included in "a", "e", "i", "o", "u"
# the second character contains one of the previously mentioned characters, and the third character is similar to the first
import nltk, re
words = ['hello', '3.354', 'John', 'random', 'INSANITY', 'guess', 'name', 'true', 'please', 'underestimated', '12', 'test!']
string = 'hello 3.354 John random INSANITY guess name true please underestimated 12 test!'
reg = r'([^aeiou][aeiou][^aeiou])*'
print([w for w in words if re.search(reg, w)])
print(nltk.re_show(reg, string))

# describe which string classes correspond to the following regular expression. \w+|[^\w\s]+.. Check results using nltk.re_show ()

# string classes: any character with one repetition or more or a character that is not a letter or digit and a space with one repetition or more. And any character except a line break
import nltk, re
words = ['hello', '3.354', 'John', 'random', 'INSANITY', 'guess', 'name', 'true', 'please', 'underestimated', '12', 'test!']
string = 'hello 3.354 John random INSANITY guess name true please underestimated 12 test!'
reg = r'\w+|[^\w\s]+.'
print([w for w in words if re.search(reg, w)])
print(nltk.re_show(reg, string))

# Describe which string classes correspond to the following regular expression. p[aeiou]{,2}t. Check results using nltk.re_show ()

# string classes: first character "p" and second character included in "a", "e", "i", "o", "u" and repeated up to two times. The last symbol is “t”
import nltk, re
words = ['hello', 'pat', 'pait', 'ppt', 'paeat', '3.354', 'John', 'random', 'INSANITY', 'guess', 'name', 'true', 'please', 'underestimated', '12', 'test!']
string = 'hello 3.354 John random INSANITY guess name true please underestimated 12 test!'
reg = r'p[aeiou]{,2}t'
print([w for w in words if re.search(reg, w)])
print(nltk.re_show(reg, string))

# write a regular expression that matches the following class of strings: an arithmetic expression with integer values and containing multiplication and addition operations (2*3+8)
import nltk, re
words = ['hello', '12*3*5', '2+3*2', '2.3*5+2.2', 'pat', 'pait', 'ppt', 'paeat', '3.354', 'John', 'random', 'INSANITY', 'guess', 'name', 'true', 'please', 'underestimated', '12', 'test!']
reg = r'^([^\D]\d*)([+|*]{1})\d*([+|*]{1})\d*$'
print([w for w in words if re.search(reg, w)])

# write a regular expression tokenize such text as don't, do and n't? 
# explain why this regular expression does not work: "n't|\w+"

# regular expression "n't|\w+" does not work because there are no brackets (group) on either side of the alternative character "|", 
# which also act as a tool to remove the snippet, but in this case, the operator "|" is not needed
import nltk, re
text = """don't take this too seriously.
        We won't make any movements until he arrives.
        Stay silent i try not to cause any problem which we can't solve now."""
pattern = r'(\w*)(n\'t)'
print(nltk.regexp_tokenize(text, pattern))
print(nltk.re_show(pattern, text))

# read help file about re.sub () function using help (re.sub)
# using re.sub, write the HTML markup removal program, replacing it with spaces
import nltk, re
text = """Aenean lacinia bibendum <a href="/life">life</a>
sed consectetur. <a href="/work">Work</a> quis risus eget
urna mollis ornare <a href="/about">about</a> leo.
"""
pattern = r'<[^>]*>'
print(text)
print(re.sub(pattern, " ", text))

# find out which of the next patterns is more popular in different corpuses:
# as best ___ can
# the best ___ can
import nltk
from nltk.corpus import gutenberg, webtext, brown
gutenberg_text = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
brown_text = nltk.Text(brown.words(categories='news'))
web_text = nltk.Text(webtext.words())

pattern = r'(?i)<as><best>(<.*>)<can>'
print("Moby Dick [as best ___ can]: ")
gutenberg_text.findall(pattern)
print("\nNews [as best ___ can]: ")
brown_text.findall(pattern)
print("\nWeb Text [as best ___ can]: ")
web_text.findall(pattern)

pattern = r'(?i)<the><best>(<.*>)<can>'
print("\nMoby Dick [the best ___ can]: ")
gutenberg_text.findall(pattern)
print("\nNews [the best ___ can]: ")
brown_text.findall(pattern)
print("\nWeb Text [the best ___ can]: ")
web_text.findall(pattern)