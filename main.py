from requests import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

API_KEY = '076373d5-29da-42b5-9212-c0d7e0149312'

start_time = time.time()

def to_dict(string):
    splittted = string.split('\n')
    s_1 = splittted[0].split(': ')
    s_1_key = s_1[0]
    s_1_value = s_1[1]
    s_2 = splittted[1].split(': ')
    s_2_key = s_2[0]
    s_2_value = s_2[1]
    a = dict()
    a[s_1_key] = s_1_value
    a[s_2_key] = s_2_value
    return a






def get_data():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Запуск без окна браузера
    driver = webdriver.Chrome()
    try:
        # Открываем страницу Flask
        driver.get("http://127.0.0.1:5000/")

        time.sleep(0.3)

        # Находим кнопку и нажимаем её
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        # Ждем, пока координаты появятся на странице
        time.sleep(0.8)

        # Ожидаем появления координат в <p id="location"> (до 5 секунд)
        location_text = driver.find_element(By.ID, "location").text
        return location_text

    except Exception as e:
        return("❌ Ошибка:", e)

    finally:
        driver.quit()  # Закрываем браузер





s = get_data()
print(s)

longitude = to_dict(s)['Долгота']
latitude = to_dict(s)['Широта']
print(longitude, latitude)

response_1 = get(f'https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={longitude},{latitude}&kind=street&results=1&format=json')
adress = response_1.json()["response"]["GeoObjectCollection"]["featureMember"][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
print(adress)

end_time = time.time()
print(end_time-start_time)