import pprint

import requests

url = 'https://github.com/'
tok = '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'


session = requests.session()
session.auth = ('s4nyo', tok)


url = ('https://api.github.com/search/code?q=eval:file+language:python+user:ubi22')
result = session.get(url)
pprint.pprint(result.json())