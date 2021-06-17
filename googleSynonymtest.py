from bs4 import BeautifulSoup
import  requests
word = "democracy"
url = 'https://www.google.co.in/search?q=define%20' + word + '#cns=1'
response = requests.get(url, headers={"user-agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0"})
html = response.content
final_soup = BeautifulSoup(html,"html5lib")

print(final_soup)