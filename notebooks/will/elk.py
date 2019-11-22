
import numpy as np
import pandas as pdfrom elasticsearch import Elasticsearch
from elasticsearch import helpers

def safe_value(field_val):
    return field_val if not pd.isna(field_val) else "Other"


es_client = Elasticsearch(http_compress=True)

def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield {
                "_index": 'your_index',
                "_type": "_doc",
                "_id" : f"{document['id']}",
                "_source": filterKeys(document),
            }
    raise StopIterationhelpers.bulk(es_client, doc_generator(your_dataframe))

helpers.bulk(es_client, doc_generator(your_dataframe))