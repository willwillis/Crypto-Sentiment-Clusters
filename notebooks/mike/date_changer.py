import os
from datetime import datetime, timedelta

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_SECRET_KEY")
DEV_ENVIRONMENT_LABEL = 'learning'
API_SCOPE = 'fullarchive'  # 'fullarchive' for full archive, '30day' for last 31 days

SEARCH_QUERY = 'bitcoin lang:en'
RESULTS_PER_CALL = 100  # 100 for sandbox, 500 for paid tiers
TO_DATE = '2019-10-31 23:59' # format YYYY-MM-DD HH:MM (hour and minutes optional)
FROM_DATE = '2019-10-31 22:59'  # format YYYY-MM-DD HH:MM (hour and minutes optional)
END_DATE = '2019-10-15 00:00'

MAX_RESULTS = 100  # Number of Tweets you want to collect

FILENAME = 'twitter-10-31-test.jsonl'  # Where the Tweets should be saved

# Script prints an update to the CLI every time it collected another X Tweets
PRINT_AFTER_X = 10

while TO_DATE>(END_DATE + timedelta(hours=1)):
    
    rule = gen_rule_payload(SEARCH_QUERY,
                            results_per_call=RESULTS_PER_CALL,
                            from_date=FROM_DATE,
                            to_date=TO_DATE
                            )
    
    TO_DATE = FROM_DATE
    
    FROM_DATE = (TO_DATE - timedelta(hours=1))
    
    print(TO_DATE)


