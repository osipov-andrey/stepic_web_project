
sudo ln -sf /home/andrey/stepik/web-mail/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill -f gunicorn
gunicorn -c /home/andrey/stepik/web-mail/etc/gunicorn_conf.py hello:app &
cd ./ask
gunicorn -c /home/andrey/stepik/web-mail/etc/gunicorn_jango.py ask.wsgi &
sudo /etc/init.d/mysql restart
mysql -u root -e "create database..."  # For Stepic
#mysql -u root -p # For My PC
