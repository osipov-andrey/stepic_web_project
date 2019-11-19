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
	start_response('200 OK', headers)
	#body = [bytes(i + '\n', 'ascii') for i in query.split('&')]
	#body = bytes('\n'.join(environ.get('QUERY_STRING').split('&')), 'ascii')
	body = [bytes('\r\n'.join(query.split('&')), encoding ='utf8')] 
	return body
