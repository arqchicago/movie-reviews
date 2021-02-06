# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:20:38 2021

@author: Ahmad
"""

from frase import parola, frase, paragrafo
from os import listdir
from os.path import isfile, join
from string import punctuation
import re


if __name__ == '__main__':

    special_char_list = list(punctuation)
    neg_folder = 'data//neg'
    pos_folder = 'data//pos'

    neg_files = [f for f in listdir(neg_folder) if isfile(join(neg_folder, f))]
    pos_files = [f for f in listdir(pos_folder) if isfile(join(pos_folder, f))]
    
    with open(neg_folder+'//'+neg_files[0], 'r') as file:
        text = file.read().replace('\n', '')

    review = paragrafo(text)
    review.remove_punctuation()
    review.remove_numeric_chars()
    review.remove_extra_spaces()
    print(review.get_paragraph())
    review.lower_case_words()
    review.remove_stop_words()
    print(review.get_paragraph())
