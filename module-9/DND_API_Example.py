import requests
import json

response = requests.get('https://www.dnd5eapi.co/api/classes/wizard')

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

#print(response.status_code)
#print(response.json())