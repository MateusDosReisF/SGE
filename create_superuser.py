import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seuprojeto.settings')
django.setup()

# Verifica se o superusuário já existe
if not User.objects.filter(username='mateus').exists():
    User.objects.create_superuser('mateus', 'email@example.com', '151211')
