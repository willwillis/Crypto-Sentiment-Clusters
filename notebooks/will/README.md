# Will's Notebooks

## Reddit Folder
- I set up a reddit API account, played with Prawl, but we probably won't go this route to mine "crypto sentiment"

## Twitter Folder

### The Firehose

- I found this site out there that hosts "sample" twitter firehose data http://files.pushshift.io/twitter/samplehose_data/. I've experimented with both their [daily](./twitter/parseFirehose.ipynb) and [hourly](./twitter/FirehoseHourly.ipynb) formats.
- The [download-hourly-send-to-pd.py](download-hourly-send-to-pd.py) script I wrote does the following:
    - Downloads Hourly Files
    - Decompresses them from the `zstandard` format to `.jsonl` files
    - converts them to a `Pandas` dataframe

### Twitter API

- [tweepy](./twitter/tweepy.ipynb) was our first attempt.
- However we settled on using the API directly with `requests` to pull data.


