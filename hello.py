#coding: utf-8

def wsgi_app(environ, start_response):

    body = ''
    query_string = environ.get('QUERY_STRING', '')
    for term in query_string.split('&'):
        body = '%s%s\r\n' % (body, term)

    start_response('200 OK', [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ])

    return iter([body.encode()])