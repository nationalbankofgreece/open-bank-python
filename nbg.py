import os

import dotenv
import requests


DOTENV_PATH = os.path.join(os.getcwd(), '.env')
if os.path.exists(DOTENV_PATH):
    dotenv.load_dotenv(DOTENV_PATH)


NBG_PRIMARY_KEY = os.getenv('NBG_PRIMARY_KEY')
NBG_SECONDARY_KEY = os.getenv('NBG_SECONDARY_KEY')

NBG_API_ROOT = 'https://nbgdemo.azure-api.net/testnodeapi'

HEADERS = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': NBG_SECONDARY_KEY,
}


def get(resource, params=None):
    if not resource[0] == '/':
        resource = '/' + resource
    url = '%s%s' % (NBG_API_ROOT, resource)
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def post(resource, body=None):
    if not resource[0] == '/':
        resource = '/' + resource
    url = '%s%s' % (NBG_API_ROOT, resource)
    response = requests.post(url, headers=HEADERS, json=body)
    return response
