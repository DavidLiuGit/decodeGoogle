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
        try:
            if (response['itemListElement'][element]['result']['description']): 
                graph[response['itemListElement'][element]['result']['name']] = {
                    'id': response['itemListElement'][element]['result']['@id'],
                    'description': response['itemListElement'][element]['result']['description']
                }
        except KeyError: 
            continue
    return graph


def getGraph(queries, maxEdges):
    graph = {}
    for keyword in queries:
        graph[keyword] = graphRes(keyword, maxEdges)
    return graph

if __name__ == "__main__":
    queries = ["Uncle Buck"]
    response = getGraph(queries, 5)
    print response
