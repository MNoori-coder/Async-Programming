import requests
import bs4


def get_html_text(course_id: int) -> str:
    url = f'https://toplearn.com/c/{course_id}'
    response = requests.get(url)
    # response.raise_for_status()
    return response.text


def get_title_from_html_text(html: str) -> str:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('.right-side h1')
    if not header:
        return 'There is no course'
    
    return header.text.strip()

for course_id in range(6130, 6141):
    html = get_html_text(course_id)
    title = get_title_from_html_text(html)
    print(title)