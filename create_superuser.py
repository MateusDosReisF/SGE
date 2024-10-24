import os
import django
from django.contrib.auth.models import User

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
# Substitua 'seuprojeto' pelo nome correto do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

django.setup()

# Verifica se o superusuário já existe
if not User.objects.filter(username='mateus').exists():
    User.objects.create_superuser('mateus', 'email@example.com', '151211')
