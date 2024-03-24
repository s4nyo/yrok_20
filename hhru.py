import requests
import pprint
domain = 'https://api.hh.ru/'

url_vacan = f'{domain}vacancies'

params = {
    'text': 'C# developer',
    'page': 1
}
result = requests.get(url_vacan, params = params).json()

items = result['items']

first = items[0]

print(first['alternate_url'])
ok = (first['url'])

result = requests.get(ok, params = params).json()
pprint.pprint(result)