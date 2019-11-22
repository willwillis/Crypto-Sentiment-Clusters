# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

from bokeh.layouts import row, widgetbox
from bokeh.models import Select, Label, TextInput, Label
from bokeh.layouts import layout, column, row, widgetbox
from bokeh.palettes import Spectral5
from bokeh.plotting import curdoc, figure
from bokeh.models import DatetimeTickFormatter
from bokeh.themes.theme import Theme
from random import shuffle
import warnings
import json
import datetime as dt

from lib.twitlib import twitter_premium_as_df

warnings.filterwarnings('ignore')

# Style 
with open('./theme.yaml','r') as infile:
    json_data = json.load(infile)


theme_doc = Theme(json=json_data)


# Load data
data = twitter_premium_as_df('../data/clean/')
data.data.set_index('created_at')

# Make 3 DataFrames (P, N, NEU)
data_P = data.loc[data['positive'] > 0.5]
data_N = data.loc[data['negative'] > 0.5]
data_NEU = data.loc[data['neutral'] > .05]

quoted_retweet_count
quoted_reply_count
quoted_quote_count

# Def update function (widgets)
def update(attrname, old, new):
    per = character.value.lower()
    par = pol_par.value.lower()
    pal = k_w.value.lower()
    if par != 'all' and per != 'all' and pal != '':

        # Plot sentiment
        new_data_P = data_P.loc[(data_P['relevant_person'].str.contains(per)==True) & (data_P['politican_party'].str.contains(par)==True) & (data_P['top_k_word'].str.contains(pal)==True)]
        dg_P = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_N = data_N.loc[(data_N['relevant_person'].str.contains(per)==True) & (data_N['politican_party'].str.contains(par)==True) & (data_N['top_k_word'].str.contains(pal)==True)]
        dg_N = new_data_N.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_NEU = data_NEU.loc[(data_NEU['relevant_person'].str.contains(per)==True) & (data_NEU['politican_party'].str.contains(par)==True) & (data_NEU['top_k_word'].str.contains(pal)==True)]
        dg_NEU = new_data_NEU.groupby([pd.Grouper(freq='5Min')]).count()

        # Add last elem
        dg_P2 = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()
        AUX = dg_P2.tail(5)
        AUX['lenght_tweet'] = 0

        fr1 = [dg_NEU, A]
        fr2 = [dg_N, A]

        dg_NEU = pd.concat(fr1)
        dg_N = pd.concat(fr2)

        r_NEU.data_source.data['x'] = dg_NEU.index
        r_NEU.data_source.data['y'] = dg_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = dg_NEU.index
        h_NEU.data_source.data['y'] = dg_NEU.lenght_tweet

        r_N.data_source.data['x'] = dg_N.index
        r_N.data_source.data['y'] = dg_N.lenght_tweet
        h_N.data_source.data['x'] = dg_N.index
        h_N.data_source.data['y'] = dg_N.lenght_tweet

        r_P.data_source.data['x'] = dg_P.index
        r_P.data_source.data['y'] = dg_P.lenght_tweet
        h_P.data_source.data['x'] = dg_P.index
        h_P.data_source.data['y'] = dg_P.lenght_tweet

        # Histogram
        frames = [new_data_N, new_data_P, new_data_NEU]
        new_data_his = pd.concat(frames)
        hist, edges = np.histogram(new_data_his['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(new_data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(new_data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(new_data_NEU)/total)*100) + '%'


    elif par != 'all' and per != 'all':

        # Plot sentiment
        new_data_P = data_P.loc[(data_P['relevant_person'].str.contains(per)==True) & (data_P['politican_party'].str.contains(par)==True)]
        dg_P = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()

        new_data_N = data_N.loc[(data_N['relevant_person'].str.contains(per)==True) & (data_N['politican_party'].str.contains(par)==True)]
        dg_N = new_data_N.groupby([pd.Grouper(freq='5Min')]).count()

        new_data_NEU = data_NEU.loc[(data_NEU['relevant_person'].str.contains(per)==True) & (data_NEU['politican_party'].str.contains(par)==True)]
        dg_NEU = new_data_NEU.groupby([pd.Grouper(freq='5Min')]).count()

        # Add last elem
        dg_P2 = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()
        AUX = dg_P2.tail(5)
        AUX['lenght_tweet'] = 0

        fr1 = [dg_NEU, A]
        fr2 = [dg_N, A]

        dg_NEU = pd.concat(fr1)
        dg_N = pd.concat(fr2)

        r_NEU.data_source.data['x'] = dg_NEU.index
        r_NEU.data_source.data['y'] = dg_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = dg_NEU.index
        h_NEU.data_source.data['y'] = dg_NEU.lenght_tweet

        r_N.data_source.data['x'] = dg_N.index
        r_N.data_source.data['y'] = dg_N.lenght_tweet
        h_N.data_source.data['x'] = dg_N.index
        h_N.data_source.data['y'] = dg_N.lenght_tweet

        r_P.data_source.data['x'] = dg_P.index
        r_P.data_source.data['y'] = dg_P.lenght_tweet
        h_P.data_source.data['x'] = dg_P.index
        h_P.data_source.data['y'] = dg_P.lenght_tweet

        # Histogram
        frames = [new_data_N, new_data_P, new_data_NEU]
        new_data_his = pd.concat(frames)
        hist, edges = np.histogram(new_data_his['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(new_data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(new_data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(new_data_NEU)/total)*100) + '%'


    elif par != 'all' and pal != '':

        # Plot sentiment
        new_data_P = data_P.loc[(data_P['top_k_word'].str.contains(pal)==True) & (data_P['politican_party'].str.contains(par)==True)]
        dg_P = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_N = data_N.loc[(data_N['top_k_word'].str.contains(pal)==True) & (data_N['politican_party'].str.contains(par)==True)]
        dg_N = new_data_N.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_NEU = data_NEU.loc[(data_NEU['top_k_word'].str.contains(pal)==True) & (data_NEU['politican_party'].str.contains(par)==True)]
        dg_NEU = new_data_NEU.groupby([pd.Grouper(freq='5Min')]).count()

        # Add last elem
        dg_P2 = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()
        AUX = dg_P2.tail(5)
        AUX['lenght_tweet'] = 0

        fr1 = [dg_NEU, A]
        fr2 = [dg_N, A]

        dg_NEU = pd.concat(fr1)
        dg_N = pd.concat(fr2)

        r_NEU.data_source.data['x'] = dg_NEU.index
        r_NEU.data_source.data['y'] = dg_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = dg_NEU.index
        h_NEU.data_source.data['y'] = dg_NEU.lenght_tweet

        r_N.data_source.data['x'] = dg_N.index
        r_N.data_source.data['y'] = dg_N.lenght_tweet
        h_N.data_source.data['x'] = dg_N.index
        h_N.data_source.data['y'] = dg_N.lenght_tweet

        r_P.data_source.data['x'] = dg_P.index
        r_P.data_source.data['y'] = dg_P.lenght_tweet
        h_P.data_source.data['x'] = dg_P.index
        h_P.data_source.data['y'] = dg_P.lenght_tweet

        # Histogram
        frames = [new_data_N, new_data_P, new_data_NEU]
        new_data_his = pd.concat(frames)
        hist, edges = np.histogram(new_data_his['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(new_data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(new_data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(new_data_NEU)/total)*100) + '%'


    elif pal != '' and per != 'all':

        # Plot sentiment
        new_data_P = data_P.loc[(data_P['top_k_word'].str.contains(pal)==True) & (data_P['relevant_person'].str.contains(per)==True)]
        dg_P = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()

        new_data_N = data_N.loc[(data_N['top_k_word'].str.contains(pal)==True) & (data_N['relevant_person'].str.contains(per)==True)]
        dg_N = new_data_N.groupby([pd.Grouper(freq='5Min')]).count()

        new_data_NEU = data_NEU.loc[(data_NEU['top_k_word'].str.contains(pal)==True) & (data_NEU['relevant_person'].str.contains(per)==True)]
        dg_NEU = new_data_NEU.groupby([pd.Grouper(freq='5Min')]).count()

        # Add last elem
        dg_P2 = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()
        AUX = dg_P2.tail(5)
        AUX['lenght_tweet'] = 0

        fr1 = [dg_NEU, A]
        fr2 = [dg_N, A]

        dg_NEU = pd.concat(fr1)
        dg_N = pd.concat(fr2)

        r_NEU.data_source.data['x'] = dg_NEU.index
        r_NEU.data_source.data['y'] = dg_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = dg_NEU.index
        h_NEU.data_source.data['y'] = dg_NEU.lenght_tweet

        r_N.data_source.data['x'] = dg_N.index
        r_N.data_source.data['y'] = dg_N.lenght_tweet
        h_N.data_source.data['x'] = dg_N.index
        h_N.data_source.data['y'] = dg_N.lenght_tweet

        r_P.data_source.data['x'] = dg_P.index
        r_P.data_source.data['y'] = dg_P.lenght_tweet
        h_P.data_source.data['x'] = dg_P.index
        h_P.data_source.data['y'] = dg_P.lenght_tweet

        # Histogram
        frames = [new_data_N, new_data_P, new_data_NEU]
        new_data_his = pd.concat(frames)
        hist, edges = np.histogram(new_data_his['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(new_data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(new_data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(new_data_NEU)/total)*100) + '%'



    elif par != 'all':

        # Plot sentiment
        new_data_P = data_P.loc[data_P['politican_party'].str.contains(par)==True]
        dg_P = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_N = data_N.loc[data_N['politican_party'].str.contains(par)==True]
        dg_N = new_data_N.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_NEU = data_NEU.loc[data_NEU['politican_party'].str.contains(par)==True]
        dg_NEU = new_data_NEU.groupby([pd.Grouper(freq='5Min')]).count()

        # Add last elem
        dg_P2 = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()
        AUX = dg_P2.tail(5)
        AUX['lenght_tweet'] = 0

        fr1 = [dg_NEU, A]
        fr2 = [dg_N, A]

        dg_NEU = pd.concat(fr1)
        dg_N = pd.concat(fr2)

        r_NEU.data_source.data['x'] = dg_NEU.index
        r_NEU.data_source.data['y'] = dg_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = dg_NEU.index
        h_NEU.data_source.data['y'] = dg_NEU.lenght_tweet

        r_N.data_source.data['x'] = dg_N.index
        r_N.data_source.data['y'] = dg_N.lenght_tweet
        h_N.data_source.data['x'] = dg_N.index
        h_N.data_source.data['y'] = dg_N.lenght_tweet

        r_P.data_source.data['x'] = dg_P.index
        r_P.data_source.data['y'] = dg_P.lenght_tweet
        h_P.data_source.data['x'] = dg_P.index
        h_P.data_source.data['y'] = dg_P.lenght_tweet

        # Histogram
        frames = [new_data_N, new_data_P, new_data_NEU]
        new_data_his = pd.concat(frames)
        hist, edges = np.histogram(new_data_his['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(new_data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(new_data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(new_data_NEU)/total)*100) + '%'


    elif pal != '':

        # Plot sentiment
        new_data_P = data_P.loc[data_P['top_k_word'].str.contains(pal)==True]
        dg_P = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_N = data_N.loc[data_N['top_k_word'].str.contains(pal)==True]
        dg_N = new_data_N.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_NEU = data_NEU.loc[data_NEU['top_k_word'].str.contains(pal)==True]
        dg_NEU = new_data_NEU.groupby([pd.Grouper(freq='5Min')]).count()

        # Add last elem
        dg_P2 = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()
        AUX = dg_P2.tail(5)
        AUX['lenght_tweet'] = 0

        fr1 = [dg_NEU, A]
        fr2 = [dg_N, A]

        dg_NEU = pd.concat(fr1)
        dg_N = pd.concat(fr2)

        r_NEU.data_source.data['x'] = dg_NEU.index
        r_NEU.data_source.data['y'] = dg_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = dg_NEU.index
        h_NEU.data_source.data['y'] = dg_NEU.lenght_tweet

        r_N.data_source.data['x'] = dg_N.index
        r_N.data_source.data['y'] = dg_N.lenght_tweet
        h_N.data_source.data['x'] = dg_N.index
        h_N.data_source.data['y'] = dg_N.lenght_tweet

        r_P.data_source.data['x'] = dg_P.index
        r_P.data_source.data['y'] = dg_P.lenght_tweet
        h_P.data_source.data['x'] = dg_P.index
        h_P.data_source.data['y'] = dg_P.lenght_tweet

        # Histogram
        frames = [new_data_N, new_data_P, new_data_NEU]
        new_data_his = pd.concat(frames)
        hist, edges = np.histogram(new_data_his['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(new_data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(new_data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(new_data_NEU)/total)*100) + '%'


    elif per != 'all':

        # Plot sentiment
        new_data_P = data_P.loc[data_P['relevant_person'].str.contains(per)==True]
        dg_P = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_N = data_N.loc[data_N['relevant_person'].str.contains(per)==True]
        dg_N = new_data_N.groupby([pd.Grouper(freq='5Min')]).count()


        new_data_NEU = data_NEU.loc[data_NEU['relevant_person'].str.contains(per)==True]
        dg_NEU = new_data_NEU.groupby([pd.Grouper(freq='5Min')]).count()

        # Add last elem
        dg_P2 = new_data_P.groupby([pd.Grouper(freq='5Min')]).count()
        AUX = dg_P2.tail(5)
        AUX['lenght_tweet'] = 0

        fr1 = [dg_NEU, A]
        fr2 = [dg_N, A]

        dg_NEU = pd.concat(fr1)
        dg_N = pd.concat(fr2)

        r_NEU.data_source.data['x'] = dg_NEU.index
        r_NEU.data_source.data['y'] = dg_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = dg_NEU.index
        h_NEU.data_source.data['y'] = dg_NEU.lenght_tweet

        r_N.data_source.data['x'] = dg_N.index
        r_N.data_source.data['y'] = dg_N.lenght_tweet
        h_N.data_source.data['x'] = dg_N.index
        h_N.data_source.data['y'] = dg_N.lenght_tweet

        r_P.data_source.data['x'] = dg_P.index
        r_P.data_source.data['y'] = dg_P.lenght_tweet
        h_P.data_source.data['x'] = dg_P.index
        h_P.data_source.data['y'] = dg_P.lenght_tweet

        # Histogram
        frames = [new_data_N, new_data_P, new_data_NEU]
        new_data_his = pd.concat(frames)
        hist, edges = np.histogram(new_data_his['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(new_data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(new_data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(new_data_NEU)/total)*100) + '%'

    else:

	# Plot sentiment
        r_P.data_source.data['x'] = data_grouped_P.index
        r_P.data_source.data['y'] = data_grouped_P.lenght_tweet
        h_P.data_source.data['x'] = data_grouped_P.index
        h_P.data_source.data['y'] = data_grouped_P.lenght_tweet

        r_N.data_source.data['x'] = data_grouped_N.index
        r_N.data_source.data['y'] = data_grouped_N.lenght_tweet
        h_N.data_source.data['x'] = data_grouped_N.index
        h_N.data_source.data['y'] = data_grouped_N.lenght_tweet

        r_NEU.data_source.data['x'] = data_grouped_NEU.index
        r_NEU.data_source.data['y'] = data_grouped_NEU.lenght_tweet
        h_NEU.data_source.data['x'] = data_grouped_NEU.index
        h_NEU.data_source.data['y'] = data_grouped_NEU.lenght_tweet


        # Histogram
        hist, edges = np.histogram(data['lenght_tweet'].tolist(), bins=50)
        hist_words.data_source.data['top'] = hist

	# Percentages
        label_P.text = '%.2f' % ((len(data_P)/total)*100) + '%'
        label_N.text = '%.2f' % ((len(data_N)/total)*100) + '%'
        label_NEU.text = '%.2f' % ((len(data_NEU)/total)*100) + '%'
       




character = Select(title='Political', value='All', options=["All" ,"Rajoy", "Sanchez", "Iglesias", "Rivera"])
pol_par = Select(title='Politic Party', value='All', options=["All" ,"PP", "PSOE", "Podemos", "Ciudadanos"])
k_w = TextInput(value='', title='Keywords')



for widget in [character, pol_par, k_w]:
    widget.on_change('value', update)


layout = layout([
    [column(plot_P)],[widgetbox(character, pol_par)],
    # [column(plot_NEU)],[ plot_N]
])

# row(column(widgetbox(character, pol_par, k_w)), ... , plot_NEU, plot_N)
curdoc().theme = theme_doc
curdoc().add_root(layout)
curdoc().title = "Twitter Debate13J"
