from elasticsearch import Elasticsearch

from config import ES_CLUSTER, ES_USERS_INDEX, ES_PAGE_SIZE


def get_users():
    users = []
    client = Elasticsearch(ES_CLUSTER)

    res = client.search(
        index=ES_USERS_INDEX,
        body={
            "size": ES_PAGE_SIZE,
            "query": {
                "match_all": {}
            }
        },
        scroll='5m'
    )
    hits = res['hits']['hits']
    users.extend([h['_source'] for h in hits])

    if len(hits) == ES_PAGE_SIZE:
        scroll_id = res['_scroll_id']

        fetch_completed = False

        while not fetch_completed:
            res = client.scroll(
                scroll='5m',
                scroll_id=scroll_id
            )
            hits = res['hits']['hits']
            users.extend([h['_source'] for h in hits])
            if len(hits) < ES_PAGE_SIZE:
                fetch_completed = True

    return users


def send_messages():
    for u in get_users():
        send_user_message(u)


def send_user_message(user):
    """
        Not implemented
    :param user:
    :return:
    """
    return None
