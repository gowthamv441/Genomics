from bs4 import BeautifulSoup
import requests
if __name__=='__main__':
    url = "www.ncbi.nlm.nih.gov/gene/5792"
    r  = requests.get("http://" +url)
    data = r.text
    soup = BeautifulSoup(data)
    pages=[]
    for link in soup.find_all('a'):
        page=link.get('href')
        #if page.find("term")!=-1:
        pages.append(page)
    for page in pages:
        if page=="/nuccore/NC_000001.11?report=fasta&from=43522238&to=43623672":
            print (url+page)
