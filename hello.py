from cgi import parse_qs

CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=16',
        '--timeout=60',
        'hello.wsgi_app',
        )
}

def wsgi_app(environment,response_handler):
    query = parse_qs(environment['QUERY_STRING'])
    response_body = ['{}={}\r\n'.format(key, value) for key, value in query]
    response_handler('200 OK', [('Content-Type', 'text/plain')])
    return response_body
