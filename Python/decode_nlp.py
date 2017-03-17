from google.cloud import language
import json


language_client = language.Client()

def analyze(text):
	document = language_client.document_from_text(text)
	# Detects the sentiment of the text
	sentiment = document.analyze_sentiment().sentiment
	
	
	data = {}
	data['text'] = text
	
	data['sentiment']= sentiment.score
	
	#print('Text: {}'.format(text))
	#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
	
	#Detects entities in text
	entities = document.analyze_entities().entities
	
	entitiesArr = []
	
	#print("Entities:")
	for entity in entities:
		#print('\t' + entity.name)
		entitiesArr.append(entity.name)
	
	data['entities'] = entitiesArr
	
	json_data = json.dumps(data)
	
	#print json_data
	return json_data
	

print(analyze("Hello from deCODE Hackathon in Montreal with Google!"))