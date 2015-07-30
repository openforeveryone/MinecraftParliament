import urllib.request
import json
from pprint import pprint

url = 'http://lda.data.parliament.uk/commonsdivisions/id/229689.json'
test = urllib.request.urlopen(url)
data = test.read()
jsonData = data.decode('utf-8')
#print(len(json))

jsonObj = json.loads(jsonData)
pprint(jsonData)
