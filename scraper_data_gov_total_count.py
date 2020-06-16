import bs4 , requests

res = requests.get('https://www.data.gov/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')
elem = soup.select('body > header > div.header.banner.frontpage-search > div > div > h4 > label > small > a')

print('Total data set on data.gov is '+elem[0].text)
