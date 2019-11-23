#import urllib.parse


#def app(environ, start_response):
#	query = environ['QUERY_STRING']
#	status = '200 OK'
#	headers = [('Content-Type', 'text/plain')]
#	start_response(status, headers)
#	body = '\r\n'.join(query.split('&'))
#	body2 = bytes(body, encoding = 'utf-8') 
#	return body2

def app(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = [str(i + '\n').encode('ascii') for i in env['QUERY_STRING'].split('&')]

    start_response(status, headers)
    return body
