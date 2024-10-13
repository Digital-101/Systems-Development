#1. Web Scraping
#-Send Get Request
import requests
url = 'https://example.com'
response = requests.get(url)
print(response.text)
#-Parse the HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
#-Extract Data
title = soup.title
print(title)
first_paragraph = soup.find('p')
print(first_paragraph.text)

#DATA CLEANING
#2. Regular Expression
import re
text = 'My email address is john@example.com'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = re.search(email_pattern, text)
print(email.group())

#3. String Manipulation
text = 'John Doe (35 years old)'
name = text.split(' ')[0] + ' ' + text.split(' ')[1]
age = text.split(' ')[2].replace('(', '').replace(')', '')
print(name)
print(age)
