from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Загружаем страницу
@app.route('/')
def index():
    return render_template('index.html')

# Получение данных от браузера
@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        return jsonify({'status': 'success', 'latitude': latitude, 'longitude': longitude})
    else:
        return jsonify({'status': 'error', 'message': 'Не удалось получить координаты'}), 400

# Добавляем GET-запрос для проверки координат
@app.route('/location', methods=['GET'])
def check_location():
    return jsonify({'status': 'waiting', 'message': 'Ожидание координат'})

if __name__ == '__main__':
    app.run()
