from google.cloud import language

def entities_text(text):
    """Detects entities in the text."""
    language_client = language.Client()

    # Instantiates a plain text document.
    document = language_client.document_from_text(text)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.doc_type == language.Document.HTML
    entities = document.analyze_entities().entities

    for entity in entities:
        print('=' * 20)
        print('{:<16}: {}'.format('name', entity.name))
        print('{:<16}: {}'.format('type', entity.entity_type))
        print('{:<16}: {}'.format('metadata', entity.metadata))
        print('{:<16}: {}'.format('salience', entity.salience))
        print('{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
			  
if __name__ == '__main__':
	entities_text("Did you know Adam West is in Batman?")