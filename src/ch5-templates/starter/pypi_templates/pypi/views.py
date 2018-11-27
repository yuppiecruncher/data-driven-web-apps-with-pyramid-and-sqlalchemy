from pyramid.view import view_config

def get_test_packages():
    return [
        {'name': 'Requests', 'version': '1.2.3'},
        {'name': 'SQlAlchemy', 'version': '2.0.0'},
        {'name': 'Pyramid', 'version': '1.7.7' }
    ]

@view_config(route_name='home', renderer='templates/home_index.pt')
def home_index(_):
    return {
    'packages': get_test_packages()
    }

@view_config(route_name='about', renderer='templates/home_about.pt')
def about(_):
    return {}
