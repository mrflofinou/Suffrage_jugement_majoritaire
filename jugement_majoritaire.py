#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# More on this here: http://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################

VOTES = 100000
MEDIAN = VOTES/2
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

MENTIONS = [
    "A rejeter",
    "Insuffisant",
    "Passable",
    "Assez Bien",
    "Bien",
    "Très bien",
    "Excellent"
]

def create_votes():
    return [
        {
            "hermione": random.randint(3, 6),
            "balou": random.randint(0, 6),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 2),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 6)
        } for _ in range(0, VOTES)
    ]

##################################################
#################### FUNCTIONS ###################
##################################################

def results_hash (votes):
    results_candidates = {}
    for candidate in CANDIDATES:
        results_candidates[candidate] = [0]*len(MENTIONS)

    for vote in votes:
        for candidate, mention in vote.items():
            results_candidates[candidate][mention] += 1
    return results_candidates

def majoritary_mention(results):
    final_results = {}
    for key in results:
        i=0
        cumulated_votes = 0
        while cumulated_votes < MEDIAN:
            cumulated_votes += results[key][i]
            if cumulated_votes > MEDIAN:
                final_results[key] = {
                    "mention": i,
                    "score": cumulated_votes
                }
            i += 1
    return final_results



##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    votes = create_votes()
    results = results_hash(votes)
    majority = majoritary_mention(results)
    #print(majority)

if __name__ == '__main__':
    main()
