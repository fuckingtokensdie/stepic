from cgi import parse_qs

def wsgi_app(environment,response_handler):
    query = parse_qs(environment['QUERY_STRING'])
    response_body = ['{}={}\r\n'.format(key, value) for key, value in query]
    response_handler('200 OK', [('Content-Type', 'text/plain')])
    return response_body
