
#import the libraries into your Python script
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Define the URL of the Glassdoor page you want to scrape
url = 'https://www.glassdoor.com.br/Vaga/brasil-data-scientist-vagas-SRCH_IL.0,6_IN36_KO7,21.htm'

#Use the requests library to retrieve the HTML content of the page
response = requests.get(url)
html = response.content

#Use Beautiful Soup to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

#Use the Chrome Developer Tools or a similar tool to inspect the page and identify the HTML tags and classes that contain the data you want to scrape
job_titles = []
for div in soup.find_all('div', {'class': 'JobDetails_jobDetailsHeader__Hd9M3'}):
    for a in div.find_all('a', {'class': 'heading_Heading__BqX5J heading_Level1__soLZs'}):
        job_titles.append(a.text.strip())
        
#Once you have scraped all the data you want, you can store it in a pandas DataFrame
df = pd.DataFrame({'Job Title': job_titles})

#You can then save the DataFrame to a CSV file
df.to_csv('glassdoor_jobs.csv', index=False)