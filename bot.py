from flask import Flask, request
import requests
from config import ACCESS_TOKEN, GROUP_ID, POST_ID

app = Flask(__name__)

def leave_comment(user_id):
    message = f"[id{user_id}|Добро пожаловать!] Спасибо за подписку!"
    url = 'https://api.vk.com/method/wall.createComment'
    payload = {
        'owner_id': f'-{GROUP_ID}',
        'post_id': POST_ID,
        'message': message,
        'access_token': ACCESS_TOKEN,
        'v': '5.154'
    }
    response = requests.post(url, data=payload)
    print(response.json())

@app.route('/new_subscriber', methods=['POST'])
def new_subscriber():
    data = request.json
    user_id = data.get('user_id')
    if user_id:
        leave_comment(user_id)
        return 'ok'
    return 'no user_id found', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)