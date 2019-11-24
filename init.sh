sudo ln -sf /home/andrey/stepik/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill -f gunicorn
#gunicorn -c ./gunicorn_jango.py ask.wsgi:qa &
gunicorn -c /home/andrey/stepik/web/etc/gunicorn_conf.py hello:app &
cd ./ask
gunicorn -c /home/andrey/stepik/web/etc/gunicorn_jango.py ask.wsgi:application &

