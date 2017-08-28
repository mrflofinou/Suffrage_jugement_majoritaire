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
            "hermione": random.randint(2, 6),
            "balou": random.randint(0, 3),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 3),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 5)
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

def sort_by(mention):
    list_results = []
    for key in mention.keys():
        list_results += [(key, (mention[key]["mention"], mention[key]["score"]))]

    for i in range(0, len(list_results) - 1):
        for j in range(0, len(list_results) - 1):
            if list_results[j+1][1] > list_results[j][1]:
                list_results[j+1], list_results[j] = list_results[j], list_results[j+1]

    return [
        {
            "name": candidate[0],
            "mention": candidate[1][0],
            "score": candidate[1][1],
        }
        for candidate in list_results
    ]


def print_results(results):
    for i, result in enumerate(results):
        name = CANDIDATES[result["name"]]
        mention = MENTIONS[result["mention"]]
        score = result["score"]*100/VOTES
        if i == 0:
            print("GANGNANT: {} avec {}% de mention {}".format(name, score, mention))
            continue
        else:
            print("- {} avec {}% de mention {}".format(name, score, mention))

##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    votes = create_votes()
    results = results_hash(votes)
    mention = majoritary_mention(results)
    sorted_candidates = sort_by(mention)
    print_results(sorted_candidates)


if __name__ == '__main__':
    main()
