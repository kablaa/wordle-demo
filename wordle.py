'''
Formats the json name with the current date and iterates over dates
until a 404 error is returned.
'''
from datetime import datetime, timedelta
from urllib import request, error as http_error
import json

URL = 'https://www.nytimes.com/svc/wordle/v2/{}.json'


for i in range(0,30):
    date = datetime.today() + timedelta(i)
    formated_date = date.strftime('%Y-%m-%d')
    req_url = URL.format(formated_date)
    print('request: ' + req_url)
    try:
        with request.urlopen(req_url) as response:
            r = json.loads(response.read())
            print('response: ' + json.dumps(r))
            print('\033[91m' +  'solution for ' + formated_date + ': ' +  r['solution'] + '\033[0m' '\n')
    except http_error.HTTPError as e:
        print(e)
        break
