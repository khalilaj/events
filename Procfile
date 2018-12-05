web: python gunicorn conference_api.wsgi --log-file -  conference_api.manage.py collectstatic --noinput; --workers=4 --bind=0.0.0.0:$PORT conference_api.settings.py
