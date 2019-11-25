Начало проекта по крусу "Web технологии" от mail.ru

For start nginx + gunicorn + django on stepik virtual machine
you need to do next (before git clone):

	sudo apt update
	sudo apt install python3.5
	sudo apt install python3.5-dev
	sudo unlink /usr/bin/python3
	sudo ln -s /usr/bin/python3.5 /usr/bin/python3
	sudo python3 -m pip install gunicorn
	sudo python3 -m pip install django==2.0
	sudo python3 -m pip install mysqlclient


If gunicorn + Django does not work on Stepik > try:

	cd ./ask
	sudo python3 manage.py runserver 0:8000
