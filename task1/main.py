from pprint import pprint
import requests
import collections
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
all_characters = resp.json()
all_characters_intelligence = {}
for characters in all_characters:
    all_characters_intelligence[characters['name']] = characters['powerstats']['intelligence']
compared_characters = {'Hulk': all_characters_intelligence['Hulk'], 'Captain America': all_characters_intelligence['Captain America'],
                       'Thanos': all_characters_intelligence['Thanos']}
compared_characters = dict(sorted(compared_characters.items(), key=lambda item: item[1]))
[most_intelligent] = collections.deque(compared_characters, maxlen=1)
print(f'The most intelligent character is {most_intelligent} ')




