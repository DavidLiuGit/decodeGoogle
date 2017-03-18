## load_ext signature
## matplotlib inline

import requests
import pprint as pp
import json

def extractID(url):
    return url[len("http://www.wikidata.org/entity/"):]

## mid = '/m/01kmd4'
mid = '/m/07dfk'
def wikiDATA(mid):
##Search Query for topic based on mid

    numProperties = 100
    query = '''SELECT DISTINCT ?entity ?entityLabel ?isWhat
    WHERE
    {
            ?entity wdt:P646 "%s".
            ?entity wdt:P31 ?isWhat.
            SERVICE wikibase:label {
                bd:serviceParam wikibase:language "en" .
            }
     }''' % mid

    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    entity = extractID(data['results']['bindings'][0]['entity']['value'])
    isWhat = extractID(data['results']['bindings'][0]['isWhat']['value'])

## print(entity)
## print(isWhat)

##Search Query based on Human Being\
## if isWhat == "Q5":
    query = '''
           PREFIX entity: <http://www.wikidata.org/entity/>
           SELECT ?propUrl ?propLabel ?valUrl ?valLabel ?picture
           WHERE
           {
                hint:Query hint:optimizer 'None' .
                {   entity:%s ?propUrl ?valUrl .
                        ?property ?ref ?propUrl .
                        ?property a wikibase:Property .
                        ?property rdfs:label ?propLabel
                }
                
                ?valUrl rdfs:label ?valLabel
                FILTER (LANG(?valLabel) = 'en') .
                OPTIONAL{ ?valUrl wdt:P18 ?picture .}
                FILTER (lang(?propLabel) = 'en' )
        }
        ORDER BY ?propUrl ?valUrl
        LIMIT %d''' % (entity, numProperties)
    ## print(query)
    
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

## Process of filtering it to have unique facts on a person
    bindings = data['results']['bindings']
    organizedBindings = {}
    for binding in bindings:
        prop = binding['propLabel']['value']
        val = binding['valLabel']['value']
        if prop not in organizedBindings:
              organizedBindings[prop] = {val}
        else:
              organizedBindings[prop].add(val)

    for x in organizedBindings:
        organizedBindings[x] = list(organizedBindings[x])

## Pretty print of JSON
    pp.pprint(organizedBindings)

    jsonResult = json.dumps(organizedBindings)
## print(type(jsonResult))
## print(jsonResult)
