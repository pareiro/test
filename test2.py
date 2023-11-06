import subprocess
import time
import sys
import os

# Получаем URL из переменной среды
url = os.environ.get("WEBSITE_URL")

if url is None:
    print("Переменная среды WEBSITE_URL не установлена.")
    exit(1)

# Функция для отправки curl и получения кода ответа
def send_curl_request(url):
    response = subprocess.check_output(["curl", "-I", url])
    response_code = response.decode("utf-8").split("\n")[0]
    return response_code

response_code = send_curl_request(url)
print(response_code)
