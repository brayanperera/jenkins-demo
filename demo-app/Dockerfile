FROM python:3.9.11-slim
RUN apt-get update && apt-get install -y gcc
RUN mkdir /code
WORKDIR /code
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --no-input
EXPOSE 8000

ENV UWSGI_WSGI_FILE=demo_app/wsgi.py
ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4
ENV UWSGI_STATIC_MAP="/static/=/code/static/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"
ENV ALLOWED_HOSTS="demoapp.brayanperera.cyou"

CMD ["uwsgi", "--show-config"]