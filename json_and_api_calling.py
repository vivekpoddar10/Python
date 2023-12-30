import requests # for api call and getting data
import sys # for passing cmd line arg
import json # for formatting the obtained json result

if len(sys.argv) != 2:
    sys.exit()

response = requests.get('https://itunes.apple.com/search?entity=song&limit=5&term='+sys.argv[1])
print(json.dumps(response.json(), indent=2))

obj = response.json()
for result in obj['results']:
    print(result['trackName'])