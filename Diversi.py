
'''
Application that finds redundant vocabulary and suggests some synonyms
'''
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter
from collections import OrderedDict
from nltk.corpus import wordnet

def main():
    while True:
        # Take the text input
        while True:
            text = input("Please copy and paste your input text here: ")
            try:
                text = str(text)
                break
            except Exception:
                print("Please input a string")
                
        while True:
            num = input("Please enter the number of words you want to get synonyms for: ")
            try:
                num = int(num)
                break
            except Exception:
                print("Please input a number")
        
        # Process the text input
        # Take only nouns, verbs, adjectives, and adverbs (Using speech tagging)
        tokenized_text = nltk.word_tokenize(text)
        tagged_text = nltk.pos_tag(tokenized_text)
        
        # Filter via tags
        four_pos = nvaa(tagged_text)

        # Find Redundant vocabulary
        noun_count = count_words(four_pos['noun'])
        
        # Create OrderedDict sorted by number of occurrences
        sorted_noun_count = sorted_counter(noun_count)

        # Take the most frequently used words of each category
        sorted_freq_nouns = sorted_counter(count_words(four_pos['noun']))
        sorted_freq_verbs = sorted_counter(count_words(four_pos['verb']))
        sorted_freq_adjs = sorted_counter(count_words(four_pos['adjective']))
        sorted_freq_advs = sorted_counter(count_words(four_pos['adverb']))
        
        # suggesting synonym from a counter dict
        print('\nmost used nouns: {suggested synonyms}')
        print_syn_list(suggest_syn_list(sorted_freq_nouns, num))
        print('\n')
        print('\nmost used verbs: {suggested synonyms}')
        print_syn_list(suggest_syn_list(sorted_freq_verbs, num))
        print('\n')
        print('\nmost used adjectives: {suggested synonyms}')
        print_syn_list(suggest_syn_list(sorted_freq_adjs, num))
        print('\n')
        print('\nmost used adverbs: {suggested synonyms}')
        print_syn_list(suggest_syn_list(sorted_freq_advs, num))
        print('\n')
        
        

# Filter via tags
def nvaa(tagged_text):
    '''
    Takes in tagged text, returns a dictionary of with four
    keys noun, verb, adjective, and adverb, and discards
    other parts of speech.
    
    Also lemmatizes each words in the lists.
    '''
    result = dict()
    result['noun'] = []
    result['verb'] = []
    result['adjective'] = []
    result['adverb'] = []
    
    lemmatizer = WordNetLemmatizer()
    
    for unit in tagged_text:
        noun = ['NN', 'NNS']
        verb = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        adj = ['JJ', 'JJR', 'JJS']
        adv = ['RB', 'RBR', 'RBS']
        tag = unit[1]
        if tag in noun:
            n = lemmatizer.lemmatize(unit[0], 'n')
            result['noun'].append(n)
        if tag in verb:
            v = lemmatizer.lemmatize(unit[0], 'v')
            result['verb'].append(v)
        if tag in adj:
            a = lemmatizer.lemmatize(unit[0], 'a')
            result['adjective'].append(a)
        if tag in adv:
            a = lemmatizer.lemmatize(unit[0], 'a')
            result['adverb'].append(unit[0])

    return result


# Find Redundant vocabulary
def count_words(input_list):
    return Counter(input_list)


# Create OrderedDict sorted by number of occurrences
def sorted_counter(input_counter):
    return OrderedDict(sorted(input_counter.items(), reverse=True, key=lambda x: x[1]))
    

# Suggest some synonyms
def suggest_syn(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.add(l.name())
    return word, synonyms


def suggest_syn_list(sorted_freq_words, num=10):
    result = []
    for i, (word, n) in enumerate(sorted_freq_words.items()):
        result.append(suggest_syn(word))
        if i > num:
            break
    return result

def print_syn_list(syn_list):
    for syns in syn_list:
        print(syns)

if __name__ == '__main__':
    main()
    