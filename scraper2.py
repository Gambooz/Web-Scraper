from bs4 import BeautifulSoup
import requests
import pandas as pd

data = []
def internshala():
  html_text1 = requests.get('https://internshala.com/internships/keywords-python/?utm_source=hp_internship_keyword_search').text
  html_text2 = requests.get('https://internshala.com/internships/keywords-python/page-2/').text
  html_text3 = requests.get('https://internshala.com/internships/keywords-python/page-3/').text


  html_text = [html_text1, html_text2, html_text3]
  for html_text_link in html_text:
    soup = BeautifulSoup( html_text_link, 'lxml')
    jobs = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')
    for prod in jobs:
      role = prod.find('h3', class_='heading_4_5 profile').text.strip('\n')
      org = prod.find('a', class_='link_display_like_text view_detail_button').text.strip().strip('\n')
      loc = prod.find('a', class_='location_link view_detail_button').text
      leng = prod.find('div', class_='item_body').text.replace('\xa0immediately', ' ').strip('\n').strip()
      amount = prod.find('span', class_='stipend').text
      details = prod.find('a', class_='btn btn-secondary view_detail_button_outline')
      data.append([role, org, loc,leng, str(amount)[2:]])


if __name__ == '__main__':
  internshala()
  df = pd.DataFrame( data, columns = ['role', 'org', 'location', 'length/duration', 'stipend'])
  df.to_csv('jobs1.csv')