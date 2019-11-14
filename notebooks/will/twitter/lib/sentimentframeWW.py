import os
import pandas as pd
from path import Path
from newsapi import NewsApiClient
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from string import punctuation
import re

# import tweepy

analyzer = SentimentIntensityAnalyzer()

# Download/Update the VADER Lexicon
nltk.download('vader_lexicon')

# tokenizer function
lemmatizer = WordNetLemmatizer()
sw = set(stopwords.words('english'))  
#adding custom stopwords to our stopwords set
custom_sw =['RT']
sw.update(custom_sw)
regex = re.compile(r"[^a-zA-Z ]")

def clean_tokens(text):
    """Cleans and tokenizes text using nltk stopwords, regex to remove symols, lemmatizer."""
    #Apply regex filter 
    regex_filter = regex.sub('', text)
    #Get Tokens
    tokens = word_tokenize(regex_filter)
    #Set to lowercase if not in Stop Words list
    lowered_sw = [word.lower() for word in tokens if word.lower() not in sw]
    #get lemmatized clean tokens
    clean_tokens = [lemmatizer.lemmatize(word) for word in lowered_sw]
    return clean_tokens

# article = tweet_text
def process_df(df,tokenize=False,sentiment=False,**kwargs):
    columns = df.columns
    if tokenize:
        df['clean_tokens'] = df['full_text'].apply(clean_tokens)
        if sentiment:
            sentiment_score_list = []
            for tweet_text in df['clean_tokens']:
                string = " ".join(tweet_text)
                sentiment_score = analyzer.polarity_scores(string)
                sentiment_score_list.append(sentiment_score)
            sentiment_df = pd.DataFrame(sentiment_score_list)
            sentiment_df.columns = ['compound','negative','neutral','positive']
            
            df = pd.concat([df, sentiment_df], axis=1)
            
            return df
        
        else:
            
            return df

    if sentiment:

        sentiment_score_list = []

        for tweet_text in df['text']:
            sentiment_score = analyzer.polarity_scores(tweet_text)
            sentiment_score_list.append(sentiment_score)

        sentiment_df = pd.DataFrame(sentiment_score_list)

        sentiment_df.columns = ['compound','negative','neutral','positive']

        df = pd.concat([df, sentiment_df], axis=1)

        return df
    
    else:
        
        return df

