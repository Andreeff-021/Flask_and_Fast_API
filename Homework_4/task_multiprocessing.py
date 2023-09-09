import requests
from multiprocessing import Process
import time
import sys

urls = ['https://gb.ru/_nuxt/img/89f1beb.png',
        'https://photocentra.ru/images/main78/781689_main.jpg',
        'https://gb.ru/_nuxt/img/6c757d5.png',
        'https://gb.ru/_nuxt/img/6cc126e.png',
        'https://gb.ru/_nuxt/img/6c83daa.png']

# urls = sys.argv


def download(url):
    response = requests.get(url)
    filename = 'pars/' + url.split('/')[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()


if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Total download time {time.time() - start_time:.2f} seconds")