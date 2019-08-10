import requests
import shutil
import time

path = 'png/' + str(time.time()) + '.png'
code_url = 'https://www.dnsexit.com/inc/authcode2.jsp'

cookies = {
    "JSESSIONID": "9BB7ED3B808F11CBA183C5D38C5283FD",
    "sns": "tQrDgEUMbAIaJvVX6hJG9wC1t8/pZoM2"
}

r = requests.get(code_url, cookies=cookies, stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)  