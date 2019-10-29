import os

MONGO_URI = os.environ['MONGO_URI']
API_VERSION = 'v1beta1'
PAGINATION = False
HATEOAS = False
SORTING = False

schema = {
    'doi': {},
    'journal': {},
    'title': {},
    'authors_list': {},
    'authors_info': {},
    'abstract': {},
    'rubric': {},
    'keywords': {},
    'references': {},
    'pages': {}
}

articles = {
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'schema': schema
}

DOMAIN = {
    'articles': articles
}