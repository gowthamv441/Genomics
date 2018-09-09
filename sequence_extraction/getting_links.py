from bs4 import BeautifulSoup
import requests
if __name__=='__main__':
    url = raw_input("Enter a website to extract the URL's from: ")
    r  = requests.get("http://" +url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))
