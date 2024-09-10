import requests
from bs4 import BeautifulSoup

# Send the HTTP request
res = requests.get("https://example.com")  # Replace with your URL

# Check if the request was successful
if res.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(res.text, 'html.parser')

    # Find all h1 tags and print them
    h1_tags = soup.find_all('h1')
    for h1 in h1_tags:
        print(h1.text)  # Print the text inside each h1 tag

else:
    print("Error: Unable to fetch the page.")
