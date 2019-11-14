import zstandard
import pathlib
import shutil
import requests
import os
import pandas as pd
import json

download_attempts = {
    "found": [],
    "missing": []
}

def decompress_zstandard(input_file):
    """input is .zst file, output is 'normal' file"""
    destination_dir = "./"
    input_file = pathlib.Path(input_file)
    with open(input_file, 'rb') as compressed:
        decomp = zstandard.ZstdDecompressor()
        output_path = pathlib.Path(destination_dir) / input_file.stem
        with open(output_path, 'wb') as destination:
            decomp.copy_stream(compressed, destination)
    filename, file_extension = os.path.splitext(input_file)
    os.rename(filename, filename + ".json")
    os.remove(input_file)
    return filename + ".json"


def filter_tweet_fields_as_dict(input_file):
    all_tweets = []
    with open(input_file, encoding='utf-8') as infile:
        for line in infile:
            data = json.loads(line)
            #pp.pprint(data)
            #break
            captured_fields = {
            "created_at" : data['created_at'],
            "screen_name" : data['user']['screen_name'],
            "full_text" : data['text'],
            "geo" : data['geo'],
            "contributors" : data['contributors'],
            "id": data["id"],
            "lang": data["lang"],
            "retweet_count": data["retweet_count"]
            }
            
            if 'extended_tweet' in data:
                captured_fields['full_text'] = data['extended_tweet']['full_text']
            #print(captured_fields)    
            all_tweets.append(captured_fields)
    return all_tweets



def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    if r.status_code == 200:
        print (f""" OK! {local_filename}""")
        download_attempts["found"].append(local_filename)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        return pathlib.Path(local_filename)
    else:
        print (f""" Unable to save {local_filename}""")
        download_attempts["missing"].append(local_filename)
        return None
    
def make_sh_hourly_url(date_string):
    # http://files.pushshift.io/twitter/samplehose_data/hourly/SH_tweets_2019-10-05-01.zst
    return f"""http://files.pushshift.io/twitter/samplehose_data/hourly/SH_tweets_2019-{date_string}.zst"""


