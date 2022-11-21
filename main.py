from bs4 import BeautifulSoup
import requests
import send_mail
import os 
import hashlib
dir_path = os.path.dirname(os.path.realpath(__file__))
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
url = 'https://www.olp.vn/tin-tức/olympic-icpc/thông-báo'
dir_path += '/'

request = requests.get(url, headers=headers)

soup = BeautifulSoup(request.text, 'html5lib')
body = soup.find('div', attrs={'role': 'main'})
contents_text = ' '.join([item.get_text() for item in body.contents])
currentHash = hashlib.sha224(contents_text.encode('utf8')).hexdigest()

with open(dir_path+'last.txt', 'r') as f1:
    last_hash = f1.readline().strip()
    print(last_hash)

if currentHash != last_hash:
    print(currentHash, last_hash)
    with open(dir_path+'last.txt', 'w') as f1:
        send_mail.send_mail()
        print(currentHash, file=f1)
   
    