#!/usr/local/bin/python3
# CSCI B551 Fall 2019
#
# Authors:[Prashanth sateesh, Aditya Kartikeya, Vansh] User ID: [psateesh, admall, vanshah]
#
#
# ./spam.py :naive bayes
#


import glob
import os
import collections
import numpy as np
import math
import sys

def mail_Dictionary(train_spam,train_not_spam):
    total_emails = [os.path.join(train_spam, f) for f in os.listdir(train_spam)]+[os.path.join(train_not_spam, f) for f in os.listdir(train_not_spam)]
    all_words = []
    for email in total_emails:
        with open(email,encoding = 'latin-1') as mail:

            for  i,line in enumerate(mail):
                words = line.split()
                all_words+=words

    m_dictionary = collections.Counter(all_words)
    list_to_remove_stuff = m_dictionary.keys()

    for item in list(list_to_remove_stuff):
        if item.isalpha() == False:
            del m_dictionary[item]
        elif len(item) == 1:
            del m_dictionary[item]

    return list(m_dictionary.keys())


def spam_Dictionary(train_spam):
    spam_emails = [os.path.join(train_spam, f) for f in os.listdir(train_spam)]
    spam_bag=[]
    for email in spam_emails:
        with open(email,encoding = 'latin-1') as mail:
            all_words = []
            for  i,line in enumerate(mail):
                words = line.split()
                for word in words:
                    if word.isalpha() == False:
                        words.remove(word)
                    elif len(word) == 1:
                        words.remove(word)
                    else:
                        all_words.append(word)
            spam_bag.append(all_words)

    return spam_bag

def ham_Dictionary(train_not_spam):
    ham_emails = [os.path.join(train_not_spam, f) for f in os.listdir(train_not_spam)]
    ham_bag=[]
    i=0
    for email in ham_emails:
        with open(email,'r',encoding = 'latin-1') as mail:
            all_words = []
            for  i,line in enumerate(mail):
                words = line.split()
                for word in words:
                    if word.isalpha() == False:
                        words.remove(word)
                    elif len(word) == 1:
                        words.remove(word)
                    else:
                        all_words.append(word)
            ham_bag.append(all_words)

    return ham_bag

def spam_matrix (m_dictionary,count_spam):

    Matrix_spam = np.full((count_spam,len(m_dictionary)),0.0006)

    return Matrix_spam

#Matrix_spam=spam_matrix(m_dictionary,count_spam)

def ham_matrix(m_dictionary, count_not_spam):
    Matrix_ham = np.full((count_not_spam, len(m_dictionary)),0.0006)

    return Matrix_ham

#Matrix_ham = ham_matrix(m_dictionary, count_not_spam)

def tokenization_spam(Matrix_s,spam_bag,m_dictionary):
    for email in range(count_spam):
     #   for j,word in enumerate(m_dictionary.keys()):
        for word in spam_bag[email]:

            if word in m_dictionary:
                ind=m_dictionary.index(word)
                Matrix_s[email][ind] = 1

    return Matrix_s

#Matrix=tokenization_spam(Matrix_spam,spam_bag,m_dictionary)

def tokenization_ham(Matrix_h,ham_bag,m_dictionary):
     for email in range(count_not_spam):
      #   for j,word in enumerate(m_dictionary.keys()):
         for word in ham_bag[email]:

             if word in m_dictionary:
                 ind=m_dictionary.index(word)
                 Matrix_h[email][ind] = 1
     return Matrix_h

#Matrix_h=tokenization_ham(Matrix_ham,ham_bag,m_dictionary)
def prob_given_class(Matrix_h,Matrix,count_spam,count_not_spam):
    ham_count=Matrix_h.sum(axis=0)
    spam_count=Matrix.sum(axis=0)
    ham_prob=np.divide(ham_count,count_not_spam)
    spam_prob=np.divide(spam_count,count_spam)
    log_ham=np.log(ham_prob)
    log_spam=np.log(spam_prob)

    return log_ham,log_spam

#log_ham,log_spam=prob_given_class(Matrix_h,Matrix,count_spam,count_not_spam)

def test(test_dir):
    test_emails = [os.path.join(test_dir, f) for f in os.listdir(test_dir)]
    basenames=[]
    for elem in test_emails:
        basenames.append(os.path.basename(elem))
    test_bag=[]
    i=0
    for email in test_emails:
        with open(email,'r',encoding = 'latin-1') as mail:

            all_words = []
            for  i,line in enumerate(mail):
                words = line.split()
                for word in words:
                    if word.isalpha() == False:
                        words.remove(word)
                    elif len(word) == 1:
                        words.remove(word)
                    else:
                        all_words.append(word)
            test_bag.append(all_words)

    return test_bag,basenames
"""test_dir= "/Users/kartik/PycharmProjects/ElemofAI/test"
test_bag,basenames= test(test_dir)
list_of_test_files=glob.glob(test_dir+"/*")
count_test=len(list_of_test_files)"""

def predict(test_bag,m_dictionary,log_ham,log_spam,prob_spam,prob_not_spam,basenames,output_file):
    predicted_list=[]
    basenames
    for email in test_bag:
        spam_word_prob=0
        ham_word_prob=0
        for word in email:
            if word in m_dictionary:
                ind = m_dictionary.index(word)
                spam_word_prob+=log_spam[ind]
                ham_word_prob+=log_ham[ind]
            if word not in m_dictionary:
                spam_word_prob += math.log(0.0006)
                ham_word_prob += math.log(0.0006)
        if  (spam_word_prob+math.log(prob_spam))> (ham_word_prob+math.log(prob_not_spam)) :
            predicted_list.append("spam")
        elif (ham_word_prob+math.log(prob_not_spam))>(spam_word_prob+math.log(prob_spam)):
            predicted_list.append("notspam")

    with open(output_file,"w") as f:
        for(basenames, predicted_list) in zip(basenames,predicted_list):
            f.write("{0} {1}\n".format(basenames,predicted_list))
    return predicted_list
#predicted_list=predict(test_bag,m_dictionary,log_ham,log_spam,prob_spam,prob_not_spam)

"""def get_test_name_and_labels(directory):
    line_list=[]
    name=[]
    mail_class=[]
    with open(directory, 'r', encoding='latin-1') as mailname:
        for line in mailname:
            line_list = line.split()
            name.append(line_list[0])
            mail_class.append(line_list[1])

    return line_list,name,mail_class
#directory="/Users/kartik/Desktop/admall-psateesh-vanshah-a3/part3/test-groundtruth.txt"
line_list,name,mail_class=get_test_name_and_labels(directory)"""

"""def mapping_list(basenames,predicted_list,name,mail_class):
    score=0
    for i,element in enumerate(basenames):
        if element in name:
            ind= name.index(element)
            if predicted_list[i]==mail_class[ind]:
                score+=1
    calc= score/len(predicted_list)
    print(calc)

    return calc
calc = mapping_list(basenames,predicted_list,name,mail_class)

"""
if __name__ == "__main__":
    train_spam = sys.argv[1]+"/spam"
    train_not_spam = sys.argv[1]+"/notspam"
    m_dictionary = mail_Dictionary(train_spam, train_not_spam)
    spam_bag = spam_Dictionary(train_spam)
    ham_bag = ham_Dictionary(train_not_spam)
    list_of_spam_files = glob.glob(sys.argv[1]+"/spam/*")
    count_spam = len(list_of_spam_files)
    list_of_not_spam_files = glob.glob(sys.argv[1] + "/notspam/*")
    count_not_spam = len(list_of_not_spam_files)
    prob_spam = count_spam / (count_not_spam + count_spam)
    prob_not_spam = count_not_spam / (count_not_spam + count_spam)
    Matrix_spam = spam_matrix(m_dictionary, count_spam)
    Matrix_ham = ham_matrix(m_dictionary, count_not_spam)
    Matrix = tokenization_spam(Matrix_spam, spam_bag, m_dictionary)
    Matrix_h = tokenization_ham(Matrix_ham, ham_bag, m_dictionary)
    log_ham, log_spam = prob_given_class(Matrix_h, Matrix, count_spam, count_not_spam)
    test_dir = sys.argv[2]
    test_bag,basenames = test(test_dir)
    list_of_test_files = glob.glob(test_dir + "/*")
    count_test = len(list_of_test_files)
    predicted_list = predict(test_bag, m_dictionary, log_ham, log_spam, prob_spam, prob_not_spam,basenames,sys.argv[3])







