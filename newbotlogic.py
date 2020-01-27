import random
snippets = [
    'I think that',
    'all is',
    'seeing that',
    'bark bark bark',
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

objects = ['toaster',
    'shoes',
    'burger',
    'bike pump',
    'happiness',
    'balls',
    'poop',
    'doodooface', ]

comp = [snippets, pronouns, verbs1, verbs2, objects]

def random_response(word):
    words = ['poop', 'toot', 'boop', 'snoot']
    words.append(word)
    response = words[random.randint(0, len(words)-1)]
    print(words)
    return response

def super_rando(user_phrase):
    amount_of_words = random.randint(2,10)
    structure = []
    x = ' '
    for i in range (0,amount_of_words):
        type_of_word = comp[random.randint(0,len(comp)-1)]
        word = type_of_word[random.randint(0,len(type_of_word)-1)]
        structure.append(word)
    return (x.join(structure))


