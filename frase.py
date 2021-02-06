# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:20:38 2021

@author: Ahmad
"""
from string import punctuation
import re
import numpy as np
from nltk.corpus import stopwords
from nltk import PorterStemmer

stop_word_list = stopwords.words("english")

class parola():

    def __init__(self, word):
        self.word = word

    def get_word(self):
        return self.word

    def get_length(self):
        return len(self.word)

    def conv_lower(self):
        self.word = self.word.lower()

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

    def levenshtein_distance(self, target, case=True):
        if case==False:
            self.word = self.word.lower()
            target = target.lower()

        n = len(self.word)
        m = len(target)
        
        if n==0:
            return m, np.zeros(shape=(0,0))
        
        if m==0:
            return n, np.zeros(shape=(0,0))
            
        matrix = np.zeros(shape=(n+1,m+1))
        matrix[0], matrix[:,0]  = range(0,m+1), range(0,n+1)
        
        s__, t__ = list(self.word), list(target)

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s__[i-1] == t__[j-1]:
                    cost = 0
                else:
                    cost = 1

                matrix[i,j] = min(matrix[i-1,j]+1, matrix[i,j-1]+1, matrix[i-1,j-1]+cost)

        return matrix[n,m], matrix

    def stem_it(self):
        stemmer = PorterStemmer()
        self.word = stemmer.stem(self.word)

        

        
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
        self.paragraph = re.sub(" \d+", " ", self.paragraph)
        
    def lower_case_words(self):
        words = self.paragraph.split()
        processed_words_list = []
        
        for word in words:
            word_processed = parola(word)
            word_processed.conv_lower()
            processed_words_list.append(word_processed.get_word())
            
        self.paragraph = ' '.join([word for word in processed_words_list])

    def remove_stop_words(self):          
        self.paragraph = ' '.join([word for word in self.paragraph.split() if word not in stop_word_list])

    def remove_words_with_length(self, length):       
        self.paragraph = ' '.join([word for word in self.paragraph.split() if len(word)!= length])

    def stemmer(self):
        words = self.paragraph.split()
        processed_words_list = []
        
        for word in words:
            word_processed = parola(word)
            word_processed.stem_it()
            processed_words_list.append(word_processed.get_word())
            
        self.paragraph = ' '.join([word for word in processed_words_list])
        
        


if __name__ == '__main__':

    new_word = parola('testing')
    
    print(new_word.get_word())
    print(new_word.get_length())
    print(new_word.get_char_count('t'))
    
    new_word.remove_char('t','')
    print(new_word.get_char_count('t'))
    
    print(new_word.get_chars_count_dict())
    print(new_word.get_chars_pct_dict())
    
    new_word.remove_char('t','', inplace=True)
    print(new_word.get_char_count('t'))
    
    
    new_sentence = frase('this is a test')
    
    print(new_sentence.get_sentence())
    print(new_sentence.get_words())
    
    words_in_sentence = new_sentence.get_words()
    
    for each_word in words_in_sentence:
        new_word = parola(each_word)
        lev_d, lev_mat = new_word.levenshtein_distance('testing', case=False)
        print("distance:", lev_d)
        print("matrix:\n")
        print(lev_mat)
        
        print(new_word.get_word())
        print(new_word.get_length())
        print(new_word.get_char_count('t'))
        
        new_word.remove_char('t','', inplace=True)
        print(new_word.get_char_count('t'))
        
        print(new_word.get_chars_count_dict())
        print(new_word.get_chars_pct_dict())
        
        new_word.remove_char('t','', inplace=True)
        print(new_word.get_char_count('t'))
        
