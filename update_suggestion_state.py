import requests
import os
import urllib

from imgurpython import ImgurClient

CLIENT_ID = '077727de8f6f20d'

# States
OPEN = '(Open)'
CLOSED = '(Closed)'

# Change this variables
ID_HASH = 'cSz0TIe_OuGZw8uNbXF0mhV'
STATE = OPEN
DESC = '현재 모든 숫자 데이터를 모으지 못해 아래의 Bar로 부터 시세 정보를 가져오고 있어 약간의 오차가 발생합니다'

client = ImgurClient(CLIENT_ID, None)

id = ID_HASH.split("_")[0]
hash = ID_HASH.split("_")[1]
desc = hash + os.linesep + STATE + os.linesep + DESC

image = client.get_image(id)
url = 'https://api.imgur.com/3/image/' + hash
headers = {'Authorization': 'Client-ID ' + CLIENT_ID}
requests.post(url, headers=headers, data={'description': desc})