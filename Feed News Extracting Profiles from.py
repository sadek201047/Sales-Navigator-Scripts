data = ''' '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')
all_data = soup.find_all('figure', class_='alert-card__image')
print(len(all_data))
for i in all_data:
	link = i.find('a', class_='block ember-view')['href']
	print('https://www.linkedin.com'+ link)