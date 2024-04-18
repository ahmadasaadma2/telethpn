import pyrogram ,time
from pytz import timezone
from datetime import datetime

api_id = 25035665
api_hash = '8ee4b0438e12bec98b3b4ad8347b851d'
client = pyrogram.Client("my_account", api_id=api_id, api_hash=api_hash)
target_timezone = timezone('Asia/Baghdad')


def change_profile_name():
    current_time = datetime.now(target_timezone).strftime("%I:%M %p")
    client.update_profile(last_name=current_time)

with client:
    while True:
        change_profile_name()
        time.sleep(30)
