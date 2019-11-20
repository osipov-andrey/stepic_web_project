#import urllib.parse


def app(environ, start_response):
	query = environ['QUERY_STRING']
	#query = urllib.parse.parse_qs(environ['QUERY_STRING'])
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	start_response(status, headers)
	body = [bytes('\r\n'.join(query.split('&')), encoding ='utf8')] 
	return body
