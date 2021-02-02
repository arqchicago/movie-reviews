# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:20:38 2021

@author: Ahmad
"""

from frase import word, sentence
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    neg_folder = 'data//neg'
    pos_folder = 'data//pos'

    neg_files = [f for f in listdir(neg_folder) if isfile(join(neg_folder, f))]
    pos_files = [f for f in listdir(pos_folder) if isfile(join(pos_folder, f))]
    
    print(pos_files)