# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

import re

#print(email_three)

def pattern_creator(list_of_words):
  pattern =r"\b({})(s|es)?\b".format("|".join(map(re.escape, list_of_words)))
  return pattern

def censor_word(word):
  pattern =r"\w|\d" 
  censor = re.sub(pattern, "*", word, flags=re.IGNORECASE)
  return censor

def list_of_matches(pattern, text):
  lst = re.findall(pattern, text, flags = re.IGNORECASE)
  lst = ["".join(item) for item in lst]
  return lst

def censorer(text, word):
  if type(word) == str:
    word = [word]
  pattern = pattern_creator(word)
  lst = list_of_matches(pattern, text)
  for item in lst:
    censor = censor_word(item)
    text = re.sub(pattern, censor, text, count=1, flags = re.IGNORECASE)  
  return text

proprietary_terms = ["Helena","she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


#print(censorer(email_one, "learning algorithm"))

def censor_negative_words(text, negative, list_of_words, number = 2):
  if type(negative) == str:
    negative = [negative]
  pattern = pattern_creator(negative)
  lst = list_of_matches(pattern, text)
  words_to_decensor = []
  for i, item in enumerate(lst):
    censor = censor_word(item)
    if i<number:
      words_to_decensor.append((censor, item))
    text = re.sub(pattern, censor, text, count=1, flags = re.IGNORECASE)
  for censor, item in words_to_decensor:
    text = text.replace(censor, item, 1)
  text = censorer(text, list_of_words)     
  return text

negative_words = ["development","turn","concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable", "unsure"]

#print(censor_negative_words(email_three, negative_words, proprietary_terms, 3))

def complete_censorship(text, list_of_words):
  text = censorer(text, list_of_words)
  pattern = r"(\w+\b)?(\W+\*+\W+)(\b\w+)?"
  lst = list_of_matches(pattern, text)  
  for phrase in lst:
    censor = censor_word(phrase)
    text = text.replace(phrase, censor, 1)
  return text

censor_words = proprietary_terms + negative_words

#print(complete_censorship("Development needs you "+email_four + "\nWe need help.", censor_words))

text = input("Input a text to censor:\n")
print("Input words or phrases to censor in the text: \n")
choice = 'Y'
list_of_words = []
while choice == 'Y':
  word = input("Type a word: ")
  list_of_words.append(word)
  choice = input("Do you wish to add another word? Y/N: ")
  while choice not in ["Y", "N"]:
    print("\nYou need to type Y (for yes) or N (for no)\n")
    choice = input("Do you wish to add another word? Y/N: ")

print(censorer(text, list_of_words))

