# Используем базовый образ Python
FROM python:3.8

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y curl

# Копируем скрипт в контейнер
COPY test2.py /app/

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Определяем переменную среды для URL сайта
ENV WEBSITE_URL http://example.com

# Запускаем скрипт при запуске контейнера
CMD ["python", "test2.py"]
