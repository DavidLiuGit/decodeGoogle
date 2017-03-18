import json 
import urllib

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
   
    for element in range(0, len(response['itemListElement'])):
        graph[response['itemListElement'][element]['result']['name']] = {
            'id': response['itemListElement'][element]['result']['@id'],
            'detailedDescription': response['itemListElement'][element]['result']['detailedDescription']['articleBody']
        }
    return graph

def getGraph(queryies, maxEdges):
    graph = {}
    for keyword in queryies:
        graph[keyword] = graphRes(keyword, maxEdges)
    return graph
