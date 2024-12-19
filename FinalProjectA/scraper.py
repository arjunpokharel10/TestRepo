import requests
from bs4 import BeautifulSoup


search_term = "data     analyst   "
search_term = '-'.join(search_term.split())
url = f"https://www.seek.com.au/{search_term}-jobs"
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=my_headers)
soup = BeautifulSoup(response.text, 'html.parser')
job_listings = soup.find_all('a', class_='_self')

for job in job_listings:
    job_title = job.get_text(strip=True)
    job_link = job.get('href')

    print(f"Job Title: {job_title}")
    print(f"Job Link: {job_link}")
    print('-' * 40)

# with open("output.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())

# print(job_listings)
