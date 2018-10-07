#coding: utf-8

def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    
    body = ''
    query_string = environ.get('QUERY_STRING', '')
    for term in query_string.split('&'):
        body = '%s%s\r\n' % (body, term)
    
    start_response(status, headers)
    return [body.encode()]