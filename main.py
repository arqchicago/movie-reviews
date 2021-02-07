# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:20:38 2021

@author: Ahmad
"""

import numpy as np
import progressbar
from time import sleep

from frase import parola, frase, paragrafo
from os import listdir
from os.path import isfile, join
from string import punctuation
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier


if __name__ == '__main__':

    # folders for the negative and positive reviews
    neg_folder = 'data//neg'
    pos_folder = 'data//pos'

    # collect list of files from the folders
    neg_files = [f for f in listdir(neg_folder) if isfile(join(neg_folder, f))]  
    pos_files = [f for f in listdir(pos_folder) if isfile(join(pos_folder, f))]

    raw_processed_data = []   
    is_positive = 0
    folder = neg_folder + '//'
    num_files = len(neg_files)
   
    # iterate through the neg and pos folders
    for files in [neg_files, pos_files]:
        i = 0
        print(f'arq_NLP> reading files from folder: {folder}')
        
        # initiating progress bar to keep track of text raw processing
        bar = progressbar.ProgressBar(maxval=num_files, widgets=[progressbar.Bar('█', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        
        # iterate through each file
        for file in files:
        
            # open one review at a time
            with open(folder+file, 'r') as f:
                text = f.read().replace('\n', '')
            
            # updating the progress
            i += 1
            bar.update(i)

            # create a paragrafo instance of the review
            review = paragrafo(text)
            
            # remove special characters in the review
            review.remove_punctuation()
            
            # remove numeric characters in the review
            review.remove_numeric_chars()
            
            # remove any extra spaces in the review
            review.remove_extra_spaces()
            
            # convert all words to lower case in the review
            review.lower_case_words()
            
            # remove stop words from the review
            review.remove_stop_words()
            
            # remove short words (they may not add too much value in the model)
            review.remove_words_with_length([1,2])
            
            # stem the words 
            #review.stemmer()
            
            
            # save processed review and the label
            raw_processed_data.append([review.get_paragraph(), is_positive])

        # update label after all negative reviews have been processed
        is_positive = 1
        
        # update folder to positive review folder after all negative reviews have been processed
        folder = pos_folder + '//'
        print('\n')

    #bar.finish()
    
    # create numpy array of review texts and labels
    raw_processed_text = np.array([i[0] for i in raw_processed_data])
    raw_processed_labels = np.array([i[1] for i in raw_processed_data])

    # create TF-IDF vector for the text
    print(f'arq_NLP> creating TF-IDF vector')
    vect = TfidfVectorizer(max_features=2000, min_df=7, max_df=0.8)
    processed_data = vect.fit_transform(raw_processed_text).toarray()
    
    # split data randomly into train and test
    print(f'arq_NLP> split data into train/test')
    X_train, X_test, y_train, y_test = train_test_split(processed_data, raw_processed_labels, test_size=0.2, random_state=0)
    train_set = {'type_X': type(X_train), 'rows_X': X_train.shape[0], 'cols_X':X_train.shape[0],
                 'type_y': type(y_train), 'rows_y': len(y_train)}
    test_set = {'type': type(X_test), 'rows': X_test.shape[0], 'cols':X_test.shape[0],
                'type_y': type(y_test), 'rows_y': len(y_test)}
    
    
    print(f'X training set: type={train_set["type_X"]},  rows={train_set["rows_X"]},  cols={train_set["cols_X"]}')
    print(f'y training set: type={train_set["type_y"]},  rows={train_set["rows_y"]}\n')
    print(f'X testing set: type={test_set["type"]},  rows={test_set["rows"]},  cols={test_set["cols"]}')
    print(f'y testing set: type={test_set["type_y"]},  rows={test_set["rows_y"]}')
    print('\n')
    
    
    print(f'arq_NLP> running RF classifier')
    rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    rf_classifier.fit(X_train, y_train)
    y_train_pred = rf_classifier.predict(X_train)
    y_test_pred = rf_classifier.predict(X_test)
    
    print(f'arq_NLP> model evaluation metrics\n')
    
    print(f'Training Set (classification report)\n')
    #print(f'-- Confusion Matrix')
    #print(confusion_matrix(y_train,y_train_pred))
    print(f' -- classification report')
    print(classification_report(y_train,y_train_pred))
    print()
    
    print(f'Testing Set (classification report)\n')
    #print(f'-- Confusion Matrix')
    #print(confusion_matrix(y_test,y_test_pred))
    print(f' -- classification report')
    print(classification_report(y_test,y_test_pred))
            
