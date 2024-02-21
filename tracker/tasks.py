import requests
from celery import shared_task
from config.settings import TELEGRAM_CHAT_ID, TELEGRAM_BOT_API_KEY
from tracker.models import Habit

bot_token = TELEGRAM_BOT_API_KEY
telegram_id = TELEGRAM_CHAT_ID
get_id_url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
send_message_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'


@shared_task
def send_message_to_bot(habit_id):
    requests.get(
        url=send_message_url,
        params={
            'chat_id': habit.user.telegram,
            'text': f'''Привет {habit.user}!
                {habit.time} в {habit.place} необходимо выполнять {habit.action} в течение {habit.duration} !'''
        }
    )
