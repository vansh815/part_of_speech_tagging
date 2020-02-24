#!/usr/local/bin/python3
# CSCI B551 Fall 2019
#
# Authors:[Prashanth sateesh, Aditya Kartikeya, Vansh] User ID: [psateesh, admall, vanshah]
#
# based on skeleton code by D. Crandall, 11/2019
#
# ./break_code.py : attack encryption
#

import time
import random
import math
import copy 
import sys
import encode
from prob_table import build_transition_probability_table
from prob_table import prob_first_letter
from prob_table import prob_document
from prob_table import initial_T_generator
from prob_table import initial_shuffle_generator
from prob_table import modify_T_and_shuffler
import numpy as np
from copy import deepcopy
# put your code here!

def break_code(string,corpus):
    T=initial_T_generator()
    shuffler=[0,2,1,3]
    string_encode=encode.encode(string,T,shuffler)
    P=prob_document(string_encode,first_letter_prob_table,transition_prob_table)
    for i in range(0,12000):
        T_dash,shuffler_dash=modify_T_and_shuffler(T,shuffler)
        string_encode_dash=encode.encode(string,T_dash,shuffler_dash)
        P_dash=prob_document(string_encode_dash,first_letter_prob_table,transition_prob_table)
        if P_dash>P:
            P=deepcopy(P_dash)
            T=deepcopy(T_dash)
            shuffler=deepcopy(shuffler_dash)
        
        else:
            toss=np.random.binomial(1,np.exp(P_dash-P))
            if toss==1:
                P=deepcopy(P_dash)
                T=deepcopy(T_dash)
                shuffler=deepcopy(shuffler_dash)
        
    string_encode_dash=encode.encode(string,T_dash,shuffler_dash)
    string_encode=encode.encode(string,T,shuffler)
    return string_encode,P
    

        
                
            
    









    



if __name__== "__main__":
    if(len(sys.argv) != 4):
        raise Exception("usage: ./break_code.py coded-file corpus output-file")
    outputfile = open(sys.argv[3],"w")
    encoded = encode.read_clean_file(sys.argv[1])
    corpus = encode.read_clean_file(sys.argv[2])
    transition_prob_table=build_transition_probability_table(corpus)
    first_letter_prob_table=prob_first_letter(corpus)
    habib_strings=[]
    habib_probs=[]
    start_time=time.time()
    
    while time.time()-start_time<450:
        yalla_s,yalla_p=break_code(encoded,corpus)
        habib_strings+=[yalla_s]
        habib_probs+=[yalla_p]
        
    ind=habib_probs.index(max(habib_probs))
    outputfile.write(habib_strings[ind])
        
    

    

