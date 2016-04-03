Create virtual environment
--------------------------
    mkdir env
    virtualenv env
    source env/bin/activate
    pip install -U -r requirements.txt


Create project
--------------
    mkdir wpa
    cd wpa
    django-admin.py startproject project .
    python ./manage.py startapp app


Synchronize database
--------------------
    python ./manage.py makemigrations
    python ./manage.py migrate

Use shell
---------
    python ./manage.py shell
