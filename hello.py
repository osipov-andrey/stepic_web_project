import urllib.parse


def wsgi_application(environ, start_response):

    if 'QUERY_STRING' in environ:
        query = environ['QUERY_STRING']
        query_parse = urllib.parse.parse_qs(query)
        # for i in query_parse:
        #     for j in query_parse[i]:
        #         print(f'{i}={j}')
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = '\n'.join([f'{i}={j}' for i in query_parse for j in query_parse[i]])
    start_response(status, headers)
    return body
