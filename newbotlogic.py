import random
import requests
from servers import server_list
import json


def switcher_func(string):
    string = string.lower()
    phrase_list = string.split()
    switcher = {
        1: super_rando(phrase_list),
        2: shmirator(phrase_list),
        3: random_server(string),
        4: bruh(phrase_list),
        
    }
    
    response = switcher.get(random.randint(1,4))
    return response

snippets = [
    'I think that',
    'all is',
    'seeing that',
    'bark bark',
    'sippin on',
    'everything in life',
]
pronouns = ['I', 'me', 'We', 'us']
verbs1 = ['have',
          'own',
          'possess',
          'lack',
          'consist',
          'involve',
          'include',
          'contain', ]

verbs2 = ['Love',
          'Like',
          'Dislike',
          'Hate',
          'Adore',
          'Prefer',
          'Care for',
          'Mind',
          'Want',
          'Need',
          'Desire',
          'Wish',
          'Hope',
          'Appreciate',
          'Value', ]
adejctives = [
    'open',
    'awake',
    'temporary',
    'handsomely',
    'plant',
    'languid',
    'special',
    'narrow',
    'lumpy',
    'awesome',
    'valuable',
    'is cancelled',


]
objects = ['toaster',
           'shoes',
           'burger',
           'bike pump',
           'happiness',
           'balls',
           'poop',
           'doodooface', ]



def random_response(word):
    words = ['poop', 'toot', 'boop', 'snoot']
    words.append(word)
    response = words[random.randint(0, len(words)-1)]
    print(words)
    return response


def super_rando(phrase_list):
    # phrase_list = user_phrase.split()
    comp = [snippets, pronouns, verbs1, verbs2, adejctives, objects, phrase_list]
    amount_of_words = random.randint(2, 10)
    structure = []
    separator = ' '
    for i in range(0, amount_of_words):
        type_of_word = comp[random.randint(0, len(comp)-1)]
        word = type_of_word[random.randint(0, len(type_of_word)-1)]
        structure.append(word)
    return (separator.join(structure))


def shmirator(phrase_list):
    # phrase_list = user_phrase.split()
    new_phrase = []
    separator = ' '
    vowels = ['a','e','i','o','u']
    for word in phrase_list:
        if len(word) <= 1 or word[0] in vowels:
            shword =  'shm'+str(word)
        else:
            shword = 'shm'+(word[1:])             
        new_phrase.append(shword)
    return (separator.join(new_phrase))

def random_server(string):
    server = server_list[random.randint(0,len(server_list)-1)]
    print(server+string)
    r = requests.get(server+string).content
    r = json.loads(r)
    r = r["message"]+'courtesy of ' + server  
    return(r)

def bruh(phrase_list):
    amount = len(phrase_list)
    bruh = 'bruh '
    response = bruh * amount
    return response
# print(bruh(['hello', 'there']))