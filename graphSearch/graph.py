import json 
import urllib

api_key = "AIzaSyBMU0S9nnRFKPsOKGON5t0QLyTxpRSHoiM"
#open("AIzaSyBMU0S9nnRFKPsOKGON5t0QLyTxpRSHoiM").read()
query = 'Taylor Swift'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for element in response['itemListElement']:
  print element['result']['name'] + ' (' + str(element['resultScore']) + ')'

