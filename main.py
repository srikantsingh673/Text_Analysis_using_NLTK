''' Text Analysis using NLTK by Rishu '''

from nltk.tokenize import word_tokenize
import textstat
import re
import nltk
from bs4 import BeautifulSoup
import html5lib
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob

url = "https://www.sciencedirect.com/topics/computer-science/food-consumption" #link of webpage
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55'}

link = requests.get(url, headers=headers)
ask = link.content
soup = BeautifulSoup(ask,'html.parser')
new = soup.get_text()
print('\n')
#print(new)
#Function to calculate Negative and positive score
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(new)
    print(score)

print("\nNegative, Neutral and positive score : ")
sentiment_analyse(new)

#Function to  Calculate Polarity and Subjectivity.
sp = TextBlob(new).sentiment 
print("Polarity and Subjectivity : ")
print(sp)

#function to find Avg sentence Length
def avg(text):
  sentences = text.split(".") #split the text into a list of sentences.
  words = text.split(" ") #split the input text into a list of separate words
  if(sentences[len(sentences)-1]==""): #if the last value in sentences is an empty string
    averg = len(words) / len(sentences)-1
  else:
    averg = len(words) / len(sentences)
  return averg
result = avg(new)
print("Average sentence length : ",result)

#convert all the uppercase letters to lowercase letters.
words = []
for word in new:
    words.append(word.lower())
#Converting list into str type to impliment in textstat function
def lts(s): 
    new = ""
    return (new.join(s))

new1 = (lts(words))
#Finding the percentage of total complex words present in the data.
cmx = textstat.difficult_words(new1) #Formula to find average complex words.
find = (cmx/len(words)*100)
print("Percentage of Complex Words : ",find)

sentences = new.split(".") #split the text into a list of sentences.
words = new.split(" ")
characters = list(new)

ari=(4.71 * (len(characters)/(len(words)) + 0.5 * (len(words))/(len(sentences)))) # Formula of Automated Readability Index (ARI)
print("Fog Index Value : ",ari)

avgword = (len(words)/(len(sentences))) #Formula of average Number of Words per sentence.
print("Average Number of Words per Sentence : ",avgword)

print("Complex Word Count : ", cmx)
print("Word count : ",len(words))

#Method of Syllable Count.
syllable_count=0
for w in characters:
      if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u' or w=='A' or w=='E' or w=='I' or w=='O' or w=='U'):
            syllable_count=syllable_count+1
sylword = (len(characters)/syllable_count)
print("The Avg number of syllables in the word is : ",sylword)

#Personal Pronuoun tagging
stop_words = set(stopwords.words('english'))
tokenized = sent_tokenize(new)
tags = []
personal_pronoun = 0
noun = 0
adjective = 0
adverb = 0
symbols = 0
for i in tokenized:
    wordsList = nltk.word_tokenize(i)
    # removing stop words from wordList
    wordsList = [w for w in wordsList if not w in stop_words]
    # Using a Tagger. Which is part-of-speech to find Personal Pronoun.
    tagged = nltk.pos_tag(wordsList)
    for i in tagged:
        if any('PP' in word for word in i):
            tags.append(i)
            personal_pronoun = personal_pronoun+1
        else:
            pass
    # Finding Total number of Noun
    for i in tagged:
        if any('NN' in word for word in i):
            tags.append(i)
            noun = noun+1
        else:
            pass
    # Finding total number of Adjective
    for i in tagged:
        if any('JJ' in word for word in i):
            tags.append(i)
            adjective = adjective+1
        else:
            pass
    # Finding total number of Adverb
    for i in tagged:
        if any('RB' in word for word in i):
            tags.append(i)
            adverb = adverb+1
        else:
            pass
    # Finding total number of Symbols
    for i in tagged:
        if any('SYM' in word for word in i):
            tags.append(i)
            symbols = symbols+1
        else:
            pass
print("Number of Personal Pronouns :", personal_pronoun)
print("Number of Nouns :", noun)
print("Number of Adjective :", adjective)
print("Number of Adverb :", adverb)
print("Number of Symbols :", symbols)
print("\n")
print(new)
