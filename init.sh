
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill -f gunicorn
gunicorn -c /home/box/web/etc/gunicorn_conf.py hello:app &
cd ./ask
gunicorn -c /home/box/web/etc/gunicorn_jango.py ask.wsgi &
#gunicorn -b 0.0.0.0:8000 ask.wsgi & # start from shell
