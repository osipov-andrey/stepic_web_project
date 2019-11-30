
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill -f gunicorn
gunicorn -c /home/box/web/etc/gunicorn_conf.py hello:app &
cd ./ask
gunicorn -c /home/box/web/etc/gunicorn_jango.py ask.wsgi &
sudo /etc/init.d/mysql restart
mysql -u root -e "create database stepic_web"  # For Stepic
#mysql -u root -p # For My PC

mysql -u root -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;" 
python3 /home/box/web/ask/manage.py makemigrations
python3 /home/box/web/ask/manage.py migrate
