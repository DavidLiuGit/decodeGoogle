import argparse

from google.cloud import language

def print_result(annotations):
    score = annotations.sentiment.score
    magnitude = annotations.sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

        print('Overall Sentiment: score is {} with magnitude of {}'.format(
            score, magnitude))

        print('Sentiment: score is {} with magnitude of {}'.format(
            score, magnitude))
        return 0

def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    language_client = language.Client()

    with open(movie_review_filename, 'r') as review_file:
        #Instantiate a plain text doc:
        document = language_client.document_from_html(review_file.read())

        #Detects sentiment in the doc:
        annotations = document.annotate_text(include_sentiment=True,
                                             include_syntax=True,
                                             include_entities=True)

        #print results:
        print_result(annotations)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'movie_review_filename',
        help='The filename of the movie review you want to analyze.')
    args = parser.parse_args()

    analyze(args.movie_review_filename)
        
