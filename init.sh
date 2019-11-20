sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill -f gunicorn
sudo gunicorn -c /home/box/web/etc/gunicorn.conf -b 0.0.0.0:8080 hello:app &

