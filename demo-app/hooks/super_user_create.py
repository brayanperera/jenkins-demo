from django.contrib.auth import get_user_model
User = get_user_model()
try:
    User.objects.create_superuser('admin', 'brayan.perera@gmail.com ', 'beyondm@123')
except Exception as e:
    print("User Exists")
