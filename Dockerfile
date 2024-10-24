FROM python:3.11-slim

WORKDIR /SGE

COPY requirements.txt /SGE/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /SGE/

EXPOSE 8000

# Realiza as migrações e cria o superusuário
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
