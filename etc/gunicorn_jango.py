#python = '/usr/bin/python3.7'
#pythonpath = '/home/andrey/stepik/web/ask' 
#working_dir = '/home/andrey/stepik/web/ask' 
#bind = '0.0.0.0:8000'
#workers = 5


CONFIG = {
        'mode': 'wsgi',
        'working_dir': 'home/andrey/stepik/web/',
        'pythonpath': '/usr/bin/python',
        'args': (
                '--bind=0.0.0.0:80',
                '--workers=5',
                '--timeout=60',
                'hello:app'
        )
}
