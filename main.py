import requests
import os

try:
    API_URL = os.environ["API_URL"]
    API_KEY = os.environ["API_KEY"]
    print('API key', API_KEY)
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    CHAT_ID = os.environ["CHAT_ID"]
except KeyError as e:
    print('ERROR variable does not found: ', str(e))
    exit(1)

def tel_send_message(text):
    TOKEN = TELEGRAM_TOKEN
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
        }
   
    r = requests.post(url,json=payload)
    print(r.content)
    return r

def get_balance_job():
    print('Getting Balance...')
    header = {'x-api-key': API_KEY}
    print(str(header))
    response = requests.get(f'{API_URL}balance', headers=header)
    result = response.json()
    text = f'Balance result: \n {result}'
    tel_send_message(text)

def get_common_symbol():
    print('Getting common symbol info...')
    header = {'x-api-key': API_KEY}
    print(str(header))
    response = requests.get(f'{API_URL}common_symbol/BTC-USDT', headers=header)
    result = response.json()
    text = f'Common symbol result: \n {result}'
    tel_send_message(text)

if __name__ == '__main__':
    get_balance_job()
    get_common_symbol()
