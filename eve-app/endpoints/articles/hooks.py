def pre_GET_articles_eissn_filter(request, lookup):
    if "eissn" in request.args:
        lookup["journal.eISSN"] = request.args["eissn"]    

def pre_GET_articles_year_filter(request, lookup):
    if "year" in request.args:
        lookup["journal.year"] = int(request.args["year"])

def pre_GET_articles_issue_filter(request, lookup):
    if "issue" in request.args:
        lookup["journal.issue"] = int(request.args["issue"])

def pre_GET_articles_id_filter(request, lookup):
    if "id" in request.args:
        lookup["_id"] = request.args["id"]

hooks = [pre_GET_articles_eissn_filter, pre_GET_articles_year_filter, pre_GET_articles_issue_filter, pre_GET_articles_id_filter]
