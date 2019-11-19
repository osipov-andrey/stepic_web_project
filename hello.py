#import urllib.parse


def app(environ, start_response):
	query = environ['QUERY_STRING']
	#query_parse = urllib.parse.parse_qs(query)
	#body = ''
	#for i in query_parse:
	#	for j in query_parse[i]:
	#		body += '{}={}\n'.format(i, j)
	#status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	#body = '\n'.join([f'{i}={j}' for i in query_parse for j in query_parse[i]])
	start_response(status, headers)
	body = bytes(i + '\n', 'ascii') for i in query.split('&')
	return body
