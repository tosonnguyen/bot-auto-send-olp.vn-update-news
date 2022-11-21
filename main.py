from bs4 import BeautifulSoup
import requests
import send_mail
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
url = 'https://www.olp.vn/tin-tức/olympic-icpc/thông-báo'
request = requests.get(url, headers=headers)
with open('data.html', 'w') as f:
    print(request.text, file=f)

with open('data.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup.prettify())
    # soup.find()
    # print(soup.div.div.div)
    body = soup.find('div', attrs={'role': 'main'})
    # print(body.section)
    _len = len(body.contents)
    with open('last.txt', 'r') as f1:
        last_len = int(f1.read())
        print(last_len)

    if _len != last_len:
        with open('last.txt', 'w') as f1:
            send_mail.send_mail()
            print(_len, file=f1)
   
    