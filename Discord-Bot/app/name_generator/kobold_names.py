import os, sys
from random import choice

short_nouns = []

with open(f'{os.path.dirname(os.path.realpath(__file__))}/short_nouns.txt','r') as short_nouns_file:
    for i in short_nouns_file.readlines():
        short_nouns.append(i.strip())

vowels = ['a','e','i','o','u']

try:
    num_names = int(sys.argv[1])
except:
    num_names = 1


def adjust_word_frequency(letter_count_freq:list=[0,524,374,189,25,5], words_list:list=short_nouns):
    words_freq_adj = []
    for i in range(0,len(short_nouns)):
        try:
            words_freq_adj.extend([short_nouns[i]] * letter_count_freq[len(short_nouns[i])-1])
        except:
            words_freq_adj.append(short_nouns[i])
    return words_freq_adj

input_words_list = adjust_word_frequency(words_list=short_nouns)

def get_kobold_names(num_names: int=1, input_words_list:list=input_words_list):
    kobold_names = []
    while len(kobold_names) < num_names:
        noun = choice(input_words_list)
        letters = list(noun.lower())
        for j in range(0,len(letters)):
            if letters[j] in vowels:
                new_letter = choice(vowels)
                if new_letter == letters[j]:
                    new_letter = choice(vowels)
                letters[j] = new_letter
        new_name = "".join(letters).title()
        if new_name not in kobold_names:
            kobold_names.append("".join(letters).title())
    return kobold_names

def possible_names_count(short_nouns:list=short_nouns):
    words_set = set()
    for i in short_nouns:
        vowel_positions = []
        for j in range(0,len(i)):
            if i[j] in vowels:
                vowel_positions.append(j)
        possible_words = []
        for j in range(0, len(i)):
            if j not in vowel_positions:
                try:
                    possible_words.append([i[j]] * len(possible_words[0]))
                except IndexError:
                    possible_words.append([i[j]])
            else:
                try:
                    possible_words.append(sorted(vowels * len(possible_words[0])))
                    for k in range(0,len(possible_words)):
                        possible_words[k] = possible_words[k] * 5
                except IndexError:
                    possible_words.append(vowels)
        for j in range(0,len(possible_words[0])):
            build_string = []
            for k in range(0, len(possible_words)):
                build_string.append(possible_words[k][j])
            new_word = "".join(build_string)
            words_set.add("".join(build_string))
            
    total_words = len(words_set)
    return total_words, words_set

if __name__ == "__main__":
    import sys
    try:
        num_names = int(sys.argv[1])
    except:
        num_names = 10
    kobold_names = get_kobold_names(num_names)
    print("\n".join(kobold_names))
