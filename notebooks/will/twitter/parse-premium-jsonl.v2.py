#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import pathlib
import pandas as pd
import os


# In[2]:


from lib.helpers import *
from lib.crypto import *
from lib.sentimentframe import process_df


# In[3]:


import pprint
pp = pprint.PrettyPrinter(indent=4)


# In[4]:


dirty_hourly = pathlib.Path('../../../data/dirty/hourly/')
jsonl_files = os.listdir(dirty_hourly)


# ## Parse/Extract data for ALL Days/files in folder

# `tilter_tweet_fields_as_dict` pulls specific fields/keys from a tweet, and returns them in a list of dicts

# In[5]:


all_tweets = []

for file in jsonl_files[0:3]:
    all_tweets.extend(filter_tweet_fields_as_dict(pathlib.Path(dirty_hourly,file)))


# In[6]:


print(len(all_tweets))


# ## Convert List of Dicts to a DataFrame

# In[7]:


all_tweets_df = pd.DataFrame(all_tweets)


# In[8]:


all_tweets_df.describe()


# In[9]:


all_tweets_df.dtypes


# ## Show tweets that contain BTC & have been quoted more than 5 times

# In[10]:


all_tweets_df[(all_tweets_df['full_text'].str.contains('BTC')) & (all_tweets_df['quoted_reply_count'] > 5)].head()


# In[11]:


len(all_tweets_df)


# # Unique User ID's and Screen Names
#     not 1:1

# In[12]:


pd.DataFrame({'screen_name': [all_tweets_df['screen_name'].nunique()],
                 'user_id': [all_tweets_df['user_id'].nunique()]
             })


# # Top 25 by Tweet

# In[13]:


all_tweets_df.groupby(['screen_name'])['id','full_text'].count().sort_values(by="id", ascending=False).head(25)


# # Top 25 by Retweets

# In[14]:


all_tweets_df.groupby(['screen_name'])['id','rt_status_id'].count().sort_values(by="rt_status_id", ascending=False).head(25)


# In[15]:


tweet_sentiment_df = process_df(all_tweets_df, tokenize=True, sentiment=True)


# In[16]:


# display(tweet_sentiment_df[(tweet_sentiment_df['quoted_quote_count'] > 5)].sort_values(by="rt_status_id", ascending=False).head())
# display(tweet_sentiment_df.dtypes)
print(tweet_sentiment_df.iloc[3]['clean_tokens'])
