import json
from elasticsearch import Elasticsearch

from config import SAMPLE_DATA_FILE, ES_CLUSTER, ES_TYPE, ES_USERS_INDEX


def load_sample_data():
    with open(SAMPLE_DATA_FILE, 'r') as f:
        obj = json.load(f)

    es = Elasticsearch(ES_CLUSTER)
    for node in obj:
        _id = node['index']
        es.index(index=ES_USERS_INDEX, doc_type=ES_TYPE, id=_id, body=node)


if __name__ == '__main__':
    load_sample_data()
