import os

import endpoints.articles
import endpoints.current_issues

MONGO_URI = os.environ['MONGO_URI']
API_VERSION = 'v1beta1'
PAGINATION = False
HATEOAS = False
SORTING = False

DOMAIN = {
    'articles': endpoints.articles.settings,
    'current_issues': endpoints.current_issues.settings
}