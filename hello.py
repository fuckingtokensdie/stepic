from cgi import parse_qs

def wsgi_app(environment,response_handler):
    parameter = parse_qs(environment['QUERY_STRING'], keep_blank_values=True)
    response_body = []
    for parameter_key, parameter_value_list in parameter.items():
        for parameter_value in parameter_value_list:
            line = '{}={}\r\n'.format(parameter_key, parameter_value)
            response_body.append(line)
    response_handler('200 OK', [('Content-Type', 'text/plain')])
    return response_body
