release: python manage.py migrate --noinput
web: gunicorn cardboard.wsgi --log-file -
worker: celery -A cardboard worker -l INFO --without-heartbeat --without-gossip --without-mingle --concurrency 3 --beat
worker-no-beat: celery -A cardboard worker -l INFO --without-heartbeat --without-gossip --without-mingle --concurrency 3
bot: python manage.py rundiscordbot
