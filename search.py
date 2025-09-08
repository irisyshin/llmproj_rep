import meilisearch
client = meilisearch.Client('http://127.0.0.1:7700/','ogcpqXaSV47OBxJUev8f-pgmmpjsrbsNaQKl7ma8-c')

def stock_search(query):
    return client.index('nasdaq').search(query)
