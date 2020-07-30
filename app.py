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

@app.route('/')
def usage():
    return '''
    USAGE:

    GET /v1/current_issues -- retreive all latest issues info

    GET /v1/articles -- retreive a set of articles

        URL parameters for /v1/articles:
        • eissn -- eissn of a journal
        • year -- year of publication
        • issue -- issue number

        Examples:

        Retreive all articles from "Vrach" journal, issue #6 / 2020
        GET /v1/articles?eissn=25877305&year=2020&issue=6

        Retreive all articles from "Vrach" journal published in 2020
        GET /v1/articles?eissn=25877305&year=2020

        Retreive all articles from "Vrach" journal stored in database
        GET /v1/articles?eissn=25877305
    '''

if __name__ == '__main__':
    app.run()
