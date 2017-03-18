import json 
import urllib
from wikidata import data  
import pprint as pp
import random

api_key = "AIzaSyBMU0S9nnRFKPsOKGON5t0QLyTxpRSHoiM"
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

def graphRes(keyword, maxEdges):
    graph = {}
    params = {
        'query': keyword,
        'limit': maxEdges,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())

    mID = response['itemListElement'][0]['result']['@id']
   
    for element in range(0, len(response['itemListElement'])):
        try:
            if (response['itemListElement'][element]['result']['description']): 
                graph[response['itemListElement'][element]['result']['name']] = {
                    #'id': response['itemListElement'][element]['result']['@id'],
                    'description': response['itemListElement'][element]['result']['description']
                }
        except KeyError: 
            continue
    graph['ID'] = mID
    return graph


def getGraph(queries):
    graph = {}
    for keyword in queries:
        graph[keyword] = graphRes(keyword, 1)
    print graph

    k = 'ID'
    IDList = []
    for q in queries:
        layer = graph.get(q, {})
        IDList.append(layer.get(k))

    wikiFacts = {}
    i = 0
    for ID in IDList: 
        IDcut = ID[3:]
        #print IDcut 
        wikiFacts[queries[i]] = data(IDcut)
        i += 1

    #package everything together 
    response = {} 
    for q in queries: 
        layer = graph.get(q, {})
        description = layer.itervalues().next()
        funFacts = wikiFacts.get(q, {})
        #print funFacts

        temp = {}
        temp['description'] = description.get('description')
        temp['funfacts'] = funFacts

        response[q] = temp

    responseJSON = json.dumps(response)
    return responseJSON 


if __name__ == "__main__": #or make this into a method 
    queries = ["apple"] # enter in the queries 
    response = getGraph(queries) 
    print response

    

    
