from datetime import datetime, timedelta
import urllib.request

url = 'https://www.nytimes.com/svc/wordle/v2/{}.json'
for i in range(0,30):
    date = datetime.today() + timedelta(i)
    req_url = url.format(date.strftime('%Y-%m-%d'))
    try:
        with urllib.request.urlopen(req_url) as response:
            r = response.read()
            print(r)
    except:
        break