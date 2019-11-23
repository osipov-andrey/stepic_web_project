sudo ln -sf /home/andrey/stepik/web-test/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill -f gunicorn
gunicorn -c ./gunicorn_conf.py hello:app &
