# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json
# TODO: replace with your own app_id and app_key
app_id = 'ecb90b8d'
app_key = 'c07b3e611d7d2c5aabf6512bbc3b1541'
language = 'en-gb'
word_id = 'Ace'
url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))