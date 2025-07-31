Инструкция:

1. Загрузите файлы на GitHub в новый репозиторий.
2. Зайдите на Render.com, создайте новый Web Service:
   - Build Command: pip install -r requirements.txt
   - Start Command: python bot.py
3. Подключите к Senler как Webhook:
   https://your-bot-name.onrender.com/new_subscriber
4. При подписке пользователя на группу будет оставлен комментарий под постом.

Комментарий выглядит так:
"[id123456|Добро пожаловать!] Спасибо за подписку!"