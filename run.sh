# source ./env/bin/activate
gunicorn main:app -c gunicornConfig.py
