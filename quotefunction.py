import pandas as pd
import numpy as np
from random import randrange
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def csv_to_dict(csv_path):
    return pd.read_csv(csv_path).to_dict('records')
quotes = None

def prepare_sentiment_quote_stash(quote_stash_path):
    global quotes
    #load the quote stash
    quotes = pd.read_csv(quote_stash_path)
    sid = SentimentIntensityAnalyzer()

    all_compounds = []
    for sentence in quotes['quote']:
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            if k == 'compound':
                all_compounds.append(ss[k])
    quotes['sentiment_score'] = all_compounds
    quotes= quotes.sort_values('sentiment_score')
    quotes['index'] = [ix for ix in range(0, len(quotes))]
    return quotes.to_dict('records')


# max_index_value = np.max(quotes['index'].values)

def gimme_a_quote(direction = None, current_index= None):
    max_index_value = 108
    rand_index = randrange(max_index_value)
    darker = None
    brighter = None


    if current_index is None:
        brighter = rand_index
    if direction == 'brighter':
        brighter = current_index
    else:
        darker = current_index
    if darker is not None:
        current_index = rand_index
        try:
            current_index = int(darker)
        except ValueError:
            current_index = rand_index
        if current_index > 0:
            rand_index = randrange(0, current_index-1)
            print('darker')
        else:
            rand_index= rand_index
    elif brighter is not None:
        try:
            current_index = int(brighter)
        except ValueError:
            current_index = rand_index
        if current_index < max_index_value -1:
            rand_index = randrange(current_index+1, max_index_value)
            print('brighter')
        else:
            rand_index = rand_index
    else:
        rand_index = rand_index
    return (rand_index)