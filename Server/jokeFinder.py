import json
import re
from collections import Counter
from pprint import pprint

with open('./jokes.json') as jsonFile:
    jokes = json.load(jsonFile)

jokesDict = {}

for joke in jokes:
    jokeSplit = re.compile('\w+').findall(jokes[joke])
    for word in jokeSplit:
        if word in jokesDict:
            jokesDict[word].append(joke)
        else: 
            jokesDict[word] = [joke]

def findJoke(keywords):
    jokeOccurences = []
    for keyword in keywords:
        if keyword in jokesDict:
            jokeOccurences.extend(jokesDict[keyword])
    if not jokeOccurences:
        return None
    return jokes[Counter(jokeOccurences).most_common(1)[0][0]]
