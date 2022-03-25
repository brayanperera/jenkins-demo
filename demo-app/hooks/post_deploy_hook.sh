python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py shell < /code/hooks/super_user_create.py