# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:20:38 2021

@author: Ahmad
"""
from string import punctuation

class parola():

    def __init__(self, word):
        self.word = word

    def get_word(self):
        return self.word

    def get_length(self):
        return len(self.word)

    def get_char_list(self):
        return list(self.word)

    def get_char_count(self, char):
        word_list = self.get_char_list()
        n = sum(1 for i in word_list if i==char)
        return n

    def remove_char(self, char, repchar, inplace=False):
        if inplace:
            self.word = self.word.replace(char, repchar)
            return 1
        else:
            replaced_word = self.word.replace(char, repchar)
            return replaced_word

    def get_chars_count_dict(self):
        chars_num_dict = {}
        unique_char_list = list(set(self.word))
        
        for char in unique_char_list:
            chars_num_dict[char] = self.get_char_count(char)
        
        return chars_num_dict

    def get_chars_pct_dict(self):
        chars_num_dict = {}
        unique_char_list = list(set(self.word))
        
        for char in unique_char_list:
            chars_num_dict[char] = self.get_char_count(char)*1.0/len(unique_char_list)
        
        return chars_num_dict


class frase():

    def __init__(self, sentence):
        self.sentence = sentence

    def get_sentence(self):
        return self.sentence
        
    def get_words(self):
        return list(self.sentence.split())


class paragrafo():

    def __init__(self, paragraph):
        self.paragraph = paragraph

    def get_paragraph(self):
        return self.paragraph

    def remove_punctuation(self):
        self.paragraph = self.paragraph.translate(str.maketrans('', '', punctuation))

    def remove_extra_spaces(self):
        self.paragraph = ' '.join(self.paragraph.split())

    def remove_numeric_chars(self):
        numeric_list = [0,1,2,3,4,5,6,7,8,9]
        self.paragraph = ' '.join([i for i in self.paragraph.split() if i not in numeric_list])

if __name__ == '__main__':

    new_word = word('testing')
    
    print(new_word.get_word())
    print(new_word.get_length())
    print(new_word.get_char_count('t'))
    
    new_word.remove_char('t','')
    print(new_word.get_char_count('t'))
    
    print(new_word.get_chars_count_dict())
    print(new_word.get_chars_pct_dict())
    
    new_word.remove_char('t','', inplace=True)
    print(new_word.get_char_count('t'))
    
    
    new_sentence = sentence('this is a test')
    
    print(new_sentence.get_sentence())
    print(new_sentence.get_words())
    
    words_in_sentence = new_sentence.get_words()
    
    for each_word in words_in_sentence:
        new_word = word(each_word)
        print(new_word.get_word())
        print(new_word.get_length())
        print(new_word.get_char_count('t'))
        
        new_word.remove_char('t','', inplace=True)
        print(new_word.get_char_count('t'))
        
        print(new_word.get_chars_count_dict())
        print(new_word.get_chars_pct_dict())
        
        new_word.remove_char('t','', inplace=True)
        print(new_word.get_char_count('t'))   