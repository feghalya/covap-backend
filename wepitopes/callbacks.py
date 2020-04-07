from pyramid.events import NewRequest

def add_cors_headers_response_callback(event):
    """Add CORS support"""
    def cors_headers(request, response):
        response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)

def includeme(config):
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)