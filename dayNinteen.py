import json
import re
from collections import Counter

'''Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
a) Read obama_speech.txt file and count number of lines and words 
b) Read michelle_obama_speech.txt file and count number of lines and words 
c) Read donald_speech.txt file and count number of lines and words
d) Read melina_trump_speech.txt file and count number of lines and words
'''

a = open("C:/Users/SAKSHI JAIN/pythonLearning/obama_speech.txt", mode = 'r')
b = open("C:/Users/SAKSHI JAIN/pythonLearning/michelle_obama_speech.txt", mode = 'r')
c = open("C:/Users/SAKSHI JAIN/pythonLearning/donald_speech.txt", mode = 'r')
d = open("C:/Users/SAKSHI JAIN/pythonLearning/melina_trump_speech.txt", mode = 'r')

def func(files):
    lines = len(files.readlines())
    return lines
print(func(a))
print(func(b))
print(func(c))
print(func(d))
a.close()
b.close()
c.close()
d.close()

"""Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries"""
o = open("C:/Users/SAKSHI JAIN/pythonLearning/countries.json", mode = 'r' )
def populated(json_file):
    countries_dict = json.load(json_file)
    values_dict = list(countries_dict.values())
    values_dict.sort(reverse=True)
    values_dict=values_dict[:10]
    for i in values_dict:
        for j in countries_dict.keys():
            if(countries_dict[j]==i):
                print(str(j)+" : "+str(countries_dict[j]))
populated(o)

#----------------------------------level2-----------------------------------------------
'''Extract all incoming email addresses as a list from the email_exchange_big.txt file.'''
f = open("email_exchange_big.txt",'w+')
def funct(files):
    for line in f:
        emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
        if emails :
            print(line)
print(funct(f))

'''Use the function, find_most_frequent_words to find: 
a) The ten most frequent words used in Obama's speech
b) The ten most frequent words used in Michelle's speech 
c) The ten most frequent words used in Trump's speech
d) The ten most frequent words used in Melina's speech'''
a = open("C:/Users/SAKSHI JAIN/pythonLearning/obama_speech.txt", mode = 'r')
b = open("C:/Users/SAKSHI JAIN/pythonLearning/michelle_obama_speech.txt", mode = 'r')
c = open("C:/Users/SAKSHI JAIN/pythonLearning/donald_speech.txt", mode = 'r')
d = open("C:/Users/SAKSHI JAIN/pythonLearning/melina_trump_speech.txt", mode = 'r')

def func(files):
    words = []
    for line in files:
        words.extend(line.split())
        counts = Counter(words)
        top_word = counts.most_common(1) 
    print(top_word)
func(a)
func(b)
func(c)
func(d)