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

analyzer = SentimentIntensityAnalyzer()
api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=api_key)

# Download/Update the VADER Lexicon
nltk.download('vader_lexicon')

# Fetch the news articles
def news_api_call(search_term,language="en",page_size=100,sort_by="relevancy",sources=None,domains=None,**kwargs):
    
    """Makes call to Googles newsapi.org service.
        -Required Parameter: search_term in form of string.  Can include multiple words: "term1 and term2"  
        -Optional Parameters: language(default="en"), page_size(default=100),sort_by(default="relevancy"),sources(default=None),domains(default=None)"""

    articles = newsapi.get_everything(
        q=search_term,
        sources=sources,
        domains=domains,
        language=language,
        page_size=page_size,
        sort_by=sort_by,
    )

    
    return articles


# tokenizer function
lemmatizer = WordNetLemmatizer()
sw = set(stopwords.words('english'))  
#adding custom stopwords to our stopwords set
custom_sw =['char','chars','say']
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

def news_api_df(articles_response,search_term,tokenize=False,sentiment=False,**kwargs):
    
    
    articles_list = []
    
    for article in articles_response['articles']:
        try:
            articles_list.append({
                "date":article['publishedAt'][:10],
                "source":article['source']['name'],
                "url":article['url'],
                "author":article['author'],
                "text":article['content'],
                "search_term":search_term
            })

        except AttributeError:
            pass
    
    articles_df = pd.DataFrame(articles_list)
    
    columns = ['date','search_term','source','url','author','text']
    
    articles_df = articles_df[columns]
    
    articles_df['text'] = articles_df['text'].astype(str)
    
    if tokenize:
    
        articles_df['clean_tokens'] = articles_df['text'].apply(clean_tokens)
        
        if sentiment:
            
            sentiment_score_list = []
            
            for article in articles_df['clean_tokens']:
                string = " ".join(article)
                sentiment_score = analyzer.polarity_scores(string)
                sentiment_score_list.append(sentiment_score)

            sentiment_df = pd.DataFrame(sentiment_score_list)
            
            sentiment_df.columns = ['compound','negative','neutral','positive']
            
            articles_df = pd.concat([articles_df, sentiment_df], axis=1)
            
            return articles_df
        
        else:
            
            return articles_df

    if sentiment:

        sentiment_score_list = []

        for article in articles_df['text']:
            sentiment_score = analyzer.polarity_scores(article)
            sentiment_score_list.append(sentiment_score)

        sentiment_df = pd.DataFrame(sentiment_score_list)

        sentiment_df.columns = ['compound','negative','neutral','positive']

        articles_df = pd.concat([articles_df, sentiment_df], axis=1)

        return articles_df
    
    else:
        
        return articles_df

def sentiment_df(search_term,**kwargs):

    """
    Wrapper for news_api_call, clean_tokens, and news_api_df

    most common syntax is df = sentiment_df("search_term",tokenize=True,sentiment=True)

    Optional Parameters for api call: language(default="en"), page_size(default=100)
    sort_by(default="relevancy"),sources(default=None),domains(default=None)
    
    """

    
    return news_api_df(news_api_call(search_term,**kwargs),search_term,**kwargs)
