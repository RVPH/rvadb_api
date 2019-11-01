import os

import endpoints.articles.settings
import endpoints.current_issues.settings

MONGO_URI = os.environ['MONGO_URI']
API_VERSION = 'v1beta1'
PAGINATION = False
HATEOAS = False
SORTING = False
X_DOMAINS = '*'

DOMAIN = {
    'articles': endpoints.articles.settings.settings,
    'current_issues': endpoints.current_issues.settings.settings
}