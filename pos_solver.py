#!/usr/local/bin/python3
# CS B551 Fall 2019, Assignment #3
#
# Your names and user ids:[Prashanth sateesh, Aditya Kartikeya, Vansh] User ID: [psateesh, admall, vanshah]

#
# (Based on skeleton code by D. Crandall)
#


import random
import math
import numpy as np
import copy


# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
def prior(label):
    count_adj = label.count("adj")
    count_adv = label.count("adv")
    count_adp = label.count("adp")
    count_conj = label.count("conj")
    count_det = label.count("det")
    count_noun = label.count("noun")
    count_num = label.count("num")
    count_pron = label.count("pron")
    count_prt = label.count("prt")
    count_verb = label.count("verb")
    count_dot = label.count(".")
    count_x = label.count("x")

    prob_all = [count_adj, count_adv, count_adp, count_conj, count_det, count_noun, count_num, count_pron,
                count_prt, count_verb, count_dot, count_x]
    return prob_all


class Solver:
    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling. Right now just returns -999 -- fix this!
    def posterior(self, model, x , y , z):
        if model == "Simple":
            return x
        elif model == "Complex":
            return z
        elif model == "HMM":
            return y
        else:
            print("Unknown algo!")

    # Do the training!
    #
    def train1(self, train_data):

        # bag of words


        data = []
        label = []
        # unique words
        for i in range(len(train_data)):
            x = train_data[i][0]
            y = train_data[i][1]
            for j in range(len(x)):
                data.append(x[j])
                label.append(y[j])




        # probabilities of noun

        prob_all = []

        count_adj = label.count("adj") / len(label)
        count_adv = label.count("adv") / len(label)
        count_adp = label.count("adp") / len(label)
        count_conj = label.count("conj") / len(label)
        count_det = label.count("det") / len(label)
        count_noun = label.count("noun") / len(label)
        count_num = label.count("num") / len(label)
        count_pron = label.count("pron") / len(label)
        count_prt = label.count("prt") / len(label)
        count_verb = label.count("verb") / len(label)
        count_dot = label.count(".") / len(label)
        count_x = label.count("x") / len(label)
        prob_all = [count_adj, count_adv, count_adp, count_conj, count_det, count_noun, count_num, count_pron,
                    count_prt, count_verb, count_dot, count_x]

        return prob_all , data , label

    # Functions for each algorithm. Right now this just returns nouns -- fixed it !
# algorithm for  naive bayes algorithm  
    def simplified(self,emission, prob_all, tags_list, s):


        prob = []
        for i in range(len(emission)):
            post_prob = []
            for j in range(len(emission[i])):
                post_prob.append(emission[i][j] * prob_all[i])

            prob.append(post_prob)

        prob = np.array(prob)
        prob = prob.T

        prob = prob.tolist()


        tags_final = []
        summ = 0
        for i in range(len(prob)):
            indexx = prob[i].index(max(prob[i]))
            try :
                x = math.log(prob[i][indexx])
            except :
                x = 1
            summ = summ + x
            tags_final.append(tags_list[indexx])

        #summ = math.log(summ)

        return tags_final, summ
# function to call transition probability  , initial word list probability 
    def train(self, train_data):
        count1 = 0.1
        count2 = 0.1
        count3 = 0.1
        count4 = 0.1
        count5 = 0.1
        count6 = 0.1
        count7 = 0.1
        count8 = 0.1
        count9 = 0.1
        count10 = 0.1
        count11 = 0.1
        count12 = 0.1
        label = []
        
        # unique words
        tags = []
        for i in range(len(train_data)):
            label = []
            y = train_data[i][1]
            for j in range(len(y)):
                label.append(y[j])
            tags.append(label)

        start_labels = []
        for i in range(len(tags)):
            start_labels.append(tags[i][0])

        y = start_labels

        for k in range(len(start_labels)):

            if y[k] == "adj":
                count1 = count1 + 1
            elif y[k] == "adv":
                count2 = count2 + 1
            elif y[k] == "adp":
                count3 = count3 + 1
            elif y[k] == "conj":
                count4 = count4 + 1
            elif y[k] == "det":
                count5 = count5 + 1
            elif y[k] == "noun":
                count6 = count6 + 1
            elif y[k] == "num":
                count7 = count7 + 1
            elif y[k] == "pron":
                count8 = count8 + 1
            elif y[k] == "prt":
                count9 = count9 + 1
            elif y[k] == "verb":
                count10 = count10 + 1
            elif y[k] == ".":
                count11 = count11 + 1
            else:
                count12 = count12 + 1
        start_p = [count1  , count2 ,
                   count3 , count4, count5
            , count6, count7, count8
            , count9 , count10 , count11,
                   count12 ]


        start_p = [count1 / len(start_labels), count2 / len(start_labels),
                   count3 / len(start_labels), count4 / len(start_labels), count5 / len(start_labels)
            , count6 / len(start_labels), count7 / len(start_labels), count8 / len(start_labels)
            , count9 / len(start_labels), count10 / len(start_labels), count11 / len(start_labels),
                   count12 / len(start_labels)]


        data = []
        label = []
        # unique words
        for i in range(len(train_data)):
            x = train_data[i][0]
            y = train_data[i][1]
            for j in range(len(x)):
                data.append(x[j])
                label.append(y[j])

        tags_list = ["adj", "adv", "adp", "conj", "det", "noun", "num", "pron", "prt", "verb", ".", "x"]
        transition = []
        for k in range(len(tags_list)):
            transition_list = []
            for j in range(len(tags_list)):
                transition_list.append(0.000000000001)
            transition.append(transition_list)

        for i in range(len(tags)):
            x = tags[i]
            for j in range(len(tags[i]) - 1):
                for k in range(len(tags_list)):
                    if tags_list[k] == x[j]:
                        index1 = k
                    if tags_list[k] == x[j + 1]:
                        index2 = k

                transition[index1][index2] = transition[index1][index2] + 1
        prob_all = prior(label)
        for i in range(len(transition)):
            for j in range(len(transition)):
                transition[i][j] = transition[i][j] / prob_all[i]



        return start_p, transition, tags_list

# function to calculate emission probability 

    def emission_probability(self, s, train_data, tags_list):
        data = []
        label = []
        # unique words
        for i in range(len(train_data)):
            x = train_data[i][0]
            y = train_data[i][1]
            for j in range(len(x)):
                data.append(x[j])
                label.append(y[j])

        emission = []

        for k in range(len(tags_list)):
            transition_list = []
            for j in range(len(s)):

                if k == 5 :
                    transition_list.append(0.01)
                else :
                    transition_list.append(0.000001)
            emission.append(transition_list)
        # print(emission)
        for i in range(len(s)):
            for j in range(len(data)):
                if s[i] == data[j]:
                    for k in range(len(tags_list)):
                        if label[j] == tags_list[k]:
                            index1 = k
                            break
                    emission[index1][i] = emission[index1][i] + 1

        prob_all = prior(label)
        for i in range(len(prob_all)):
            for j in range(len(emission[0])):
                emission[i][j] = float(emission[i][j] / prob_all[i])


        return emission

# algorithm for gibb's sampling 
    def complex_mcmc(self, s , transition, tags_list , emission, prob_all):
        sample_list = ["noun"] * len(s)
        sample = []
        for i in range(1000):
            post_prob = 0
            for j in range(len(s)):

                prob = []

                if j == 0:
                    for k in range(len(tags_list)):
                        temp2 = emission[k][j] * prob_all[k]
                        prob.append(temp2)
                    summ = sum(prob)
                    for k in range(len(prob)):
                        prob[k] = prob[k] / summ

                    accumulated = [0] * len(prob)

                    r = random.uniform(0, 1)

                    for k in range(len(prob)):

                        accumulated[k] = sum(prob[:k + 1])
                        if r <= accumulated[k]:
                            index = k
                            break

                    sample_list[j] = tags_list[index]

                elif j == len(s) - 1:

                    for k in range(len(tags_list)):
                        temp2 = emission[k][j] * transition[index][k] * transition[0][k] * prob_all[k]
                        prob.append(temp2)

                    summ = sum(prob)
                    for k in range(len(prob)):
                        prob[k] = prob[k] / summ
                    accumulated = [0] * len(prob)
                    r = random.uniform(0, 1)
                    for k in range(len(prob)):

                        accumulated[k] = sum(prob[:k + 1])
                        if r <= accumulated[k]:
                            index = k
                            break

                    sample_list[j] = tags_list[index]

                else:
                    for k in range(len(tags_list)):
                        temp2 = emission[k][j] * transition[index][k] * prob_all[k]
                        prob.append(temp2)

                    summ = sum(prob)
                    for k in range(len(prob)):
                        prob[k] = prob[k] / summ

                    accumulated = [0] * len(prob)

                    r = random.uniform(0, 1)

                    for k in range(len(prob)):

                        accumulated[k] = sum(prob[:k + 1])
                        if r <= accumulated[k]:
                            index = k
                            break

                    sample_list[j] = tags_list[index]
                
                if i == 999:
                    try :
                        temp1 = math.log(temp2)
                    except :
                        temp1 = 1
                    post_prob = post_prob + temp1
                



            x = copy.copy(sample_list)
            sample.append(x)
            
        
        sample = np.array(sample)
        sample = sample.T
        maxx = []
        sample = sample.tolist()
        for i in range(len(sample)):
            count_all = prior(sample[i])
            maxx.append(count_all.index(max(count_all)))
        tags_final = []
        for i in range(len(maxx)):
            for k in range(len(tags_list)):
                if maxx[i] == k:
                    tags_final.append(tags_list[k])

        return tags_final , post_prob/3.7

## algorithm of viterbi implementation 
        
    def hmm_viterbi(self,s, tags_list, start_p, transition, emission):
        matrix = [{}]
        for i in range(len(tags_list)):
            matrix[0][i] = {"p": start_p[i] * emission[i][0], "state": None}

        for i in range(1, len(s)):
            matrix.append({})
            for j in range(len(tags_list)):
                maxx = matrix[i - 1][0]["p"] * transition[0][j]  # type:
                pr = str(0)
                for k in range(1, len(tags_list)):
                    transition_p = matrix[i - 1][k]["p"] * transition[k][j]
                    if transition_p > maxx:
                        maxx = transition_p
                        pr = str(k)

                x = maxx * emission[j][i]
                matrix[i][j] = {"p": x, "state": pr}

        track = []

        maxx = max(value["p"] for value in matrix[-1].values())
        pr = None
        try :
            proba = math.log(maxx)
        except :
            proba = 1


        for value, all in matrix[-1].items():
            if all["p"] == maxx:
                track.append(value)
                pr = int(value)

                break

        for i in range(len(matrix) - 2, -1, -1):
            track.insert(0, matrix[i + 1][pr]["state"])
            pr = int(matrix[i + 1][pr]["state"])

        tags = []
        for i in range(len(track)):
            for k in range(len(tags_list)):
                if k == int(track[i]):
                    tags.append(tags_list[k])



        return tags , proba


    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It should return a list of part-of-speech labelings of the sentence, one
    #  part of speech per word.
    #
    def solve(self, model, sentence , prob_all ,tags_list, start_p ,transition, emission):
        if model == "Simple":
            return self.simplified(emission, prob_all, tags_list, sentence)
        elif model == "Complex":
            return self.complex_mcmc(sentence, transition, tags_list, emission, prob_all)
        elif model == "HMM":
            return self.hmm_viterbi(sentence, tags_list, start_p, transition, emission)



        else:
            print("Unknown algo!")

