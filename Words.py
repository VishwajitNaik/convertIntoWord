import requests
import re
from bs4 import BeautifulSoup

# Replace the URL below with the link to your Google Doc file
url = 'https://docs.google.com/document/d/1yBkgjR-9KBMZXM3G89oWiMSrtL9goY47Usw0wxE7ROo/edit'

# Get the content of the document
response = requests.get(url)
content = response.text

# Remove symbols and equations using regex
text = re.sub(r'[^\w\s]+', '', content)

# Use BeautifulSoup to extract text from HTML
soup = BeautifulSoup(text, 'html.parser')
text = soup.get_text()

# Print the final output
print(text)
