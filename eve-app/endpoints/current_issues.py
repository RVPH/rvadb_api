aggregation_pipeline = [{
    
    '$sort': {
        'journal.year': -1,
        'journal.issue': -1
    }
}, {
    '$group': {
        '_id': '$journal.eISSN',
        'volume': {
            '$first': '$journal.volume'
        },
        'year': {
            '$first': '$journal.year'
        },
        'month': {
            '$first': '$journal.month'
        },
        'issue': {
            '$first': '$journal.issue'
        }
    }

}]

settings = {
    'datasource': {
        'source': 'articles',
        'aggregation': {
            'pipeline': aggregation_pipeline

        }
    }
}