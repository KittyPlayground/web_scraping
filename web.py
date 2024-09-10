import csv
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.geeksforgeeks.org/fundamentals-of-algorithms/")  # Replace with your URL

if res.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(res.text, 'html.parser')



    # Open a CSV file for writing

   # with open('web_scraping.csv', 'w', newline='') as csvfile:
      #  csvwriter = csv.writer(csvfile)

        # Find all h2 tags and paragraphs
       # h2_tags = soup.find_all('h2')
        #for h2 in h2_tags:
            #h2_text = h2.text.strip()
            #p1 = h2.find_next('p')
            #p1_text = p1.text.strip() if p1 else ''
           # print(f"{h2_text}")
            #print(f"{p1_text}")

            #csvwriter.writerow([h2_text, p1_text])

#else:
    #print("Request failed :", res.status_code)

    #get all image url
    for img in soup.find_all('img'):
     print(img.get('src'))
    #save all image as file
    for img in soup.find_all('img'):
        img_url = img.get('src')
        img_data = requests.get(img_url).content
        with open(img_url.split('/')[-1], 'wb') as handler:
            handler.write(img_data)

















