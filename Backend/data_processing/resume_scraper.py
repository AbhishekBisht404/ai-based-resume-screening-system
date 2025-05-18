#To scrape resumes from https://www.postjobfree.com using python web scraping framework - beautiful soup
#and module requests(to interact with the apis)
import time
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.postjobfree.com/resumes?q=web+developer%2c+software+engineer%2c+data+analyst%2c+devops+engineer%2c+cybers+security&l=&radius=100&r=100&p=5'
#https://www.postjobfree.com/resumes?q=web+developer%2c+software+engineer%2c+data+analyst%2c+devops+engineer%2c+cybers+security&l=&radius=100&r=100&p=5')
#https://www.postjobfree.com/resumes?q=web+developer%2c+software+engineer%2c+data+analyst%2c+devops+engineer%2c+cybers+security&l=&radius=100&r=100&p=4'
#https://www.postjobfree.com/resumes?q=web+developer%2c+software+engineer%2c+data+analyst%2c+devops+engineer%2c+cybers+security&l=&radius=100&r=100&p=3')
#https://www.postjobfree.com/resumes?q=web+developer%2c+software+engineer%2c+data+analyst%2c+devops+engineer%2c+cybers+security&l=&radius=100&r=100&p=2'
#'https://www.postjobfree.com/resumes?q=web+developer%2C+software+engineer%2C+data+analyst%2C+devops+engineer%2C+cybers+security&n=&t=&d=&l=&radius=100&r=100'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

title_tags = soup.find_all('h3', attrs={'class': 'itemTitle'})
links = []
results = []

for title_tag in title_tags:
    links.append('https://www.postjobfree.com' + title_tag.a['href'])

for link in links:
    res = requests.get(link)
    print(res.status_code, link)
    content = BeautifulSoup(res.content, 'html.parser')
    job_title = None
    resume_content = None

    try:
        job_title_tag = content.find('h1')
        if job_title_tag:
            job_title = job_title_tag.get_text().strip()
        resume_tag = content.find('div', attrs={'class': 'normalText'})
        if resume_tag:
            resume_content = resume_tag.get_text().strip()

    except Exception as e:
        print(f"Error extracting data from {link}: {e}")
    if job_title and resume_content:
        results.append({
            'job_title': job_title,
            'resume': resume_content
        })

    time.sleep(3)

with open('../datasets/resumes.csv', 'a', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("Scraping complete.")
