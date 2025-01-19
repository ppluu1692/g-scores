FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=backend.settings \
    DATABASE_NAME=gscores_db \
    DATABASE_USER=postgres \
    DATABASE_PASSWORD=123 \
    DATABASE_HOST=postgres-app \
    DATABASE_PORT=5432 \
    DATA_PATH="/app/dataset/diem_thi_thpt_2024.csv"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]