from eve import Eve

def pre_GET(resource, request, lookup):
    if "eissn" in request.args:
        lookup["journal.eISSN"] = request.args["eissn"]    
    if "year" in request.args:
        lookup["journal.year"] = int(request.args["year"])
    if "issue" in request.args:
        lookup["journal.issue"] = int(request.args["issue"])

def on_fetched_resource(resource, response):
    for document in response['_articles']:
        del(document['_etag'])
        del(document['_created'])
        del(document['_updated'])

app = Eve()
app.on_pre_GET += pre_GET
app.on_fetched_resource += on_fetched_resource

if __name__ == '__main__':
    app.run()