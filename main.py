import requests
import os

try:
    API_URL = os.environ["API_URL"]
    API_KEY = os.environ["API_KEY"]
except KeyError as e:
    print('ERROR variable does not found: ', str(e))
    exit(1)

def get_balance_job():
    header = {'x-api-key': API_KEY}
    response = requests.get(f'{API_URL}balance', headers=header)
    print(response.json())

if __name__ == '__main__':
    get_balance_job()