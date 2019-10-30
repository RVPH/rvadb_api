from eve import Eve

import endpoints.articles.hooks

def on_fetched_resource(resource, response):
    for document in response['_items']:
        del(document['_etag'])
        del(document['_created'])
        del(document['_updated'])

app = Eve()

for hook in endpoints.articles.hooks.hooks:
    app.on_pre_GET_articles += hook

app.on_fetched_resource += on_fetched_resource

if __name__ == '__main__':
    app.run()