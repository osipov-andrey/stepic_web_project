For start nginx + gunicorn + django on stepik virtual machine
you need to do next:

1) launch update.sh
2) launch init.sh

If gunicorn + Django does not work on Stepik > try:

    cd ./ask
	sudo python3 manage.py runserver 0:8000
	
If you take Error "django.db.utils.IntegrityError: 
(1048, "Column 'last_login' cannot be null")" do next:

    $ mysql
    mysql> SELECT * FROM django_migrations;
    mysql> TRUNCATE TABLE django_migrations;
    
    Leave MySQL terminal, and run the migrations again in django:
    $ python manage.py migrate --fake-initial
    
    Make sure this message appears:
    0005_alter_user_last_login_null - [OK]
    
    Restart init.sh