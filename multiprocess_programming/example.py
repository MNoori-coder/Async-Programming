import requests
import bs4
import datetime
from concurrent.futures import ThreadPoolExecutor as PoolExcecutor
# from concurrent.futures import ProcessPoolExecutor as PoolExcecutor
import multiprocessing

def get_title(url: str) -> str:
    p = multiprocessing.current_process()
    print(f'Process ID: {p.pid}, Process name: {p.name}')
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    tag = soup.select_one('title')

    if not tag:
        return 'None'
    return tag.text.strip()


def main():
    t0 = datetime.datetime.now()
    urls = [
        'https://mohamadnoori.ir',
        'https://toplearn.com',
        'https://learnby.ir',
        'https://barnamenevisan.info',
        'https://toplearn.com/c/6140',
        'https://divar.ir/'
    ]

    tasks = []
    with PoolExcecutor() as executor:
        for url in urls:
            f = executor.submit(get_title, url)
            tasks.append(f)

        print('Waiting...', flush=True)

    t1 = datetime.datetime.now() - t0
    print(f'Tasks finished in {t1.total_seconds():.2f} seconds')

    for task in tasks:
        print(f'{task.result()}')

if __name__ == '__main__':
    main()
