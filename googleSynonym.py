import requests
import urllib.request	

word = input("Write down a single word : ")

url = 'https://www.google.com/search?q=define+' + word

my_request = requests.get(url)

my_HTML = my_request.text

print(my_HTML)