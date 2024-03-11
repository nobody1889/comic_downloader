from comic_reader import (Founder, Downloader)
import time


def read_manga(url):
    app = Founder(url)
    app.search_html(tage="img")
    links = app.get_link()
    return links


def download_manga(the_list, file_name):
    start = time.time()
    app = Downloader()
    app.set(images=the_list, save_as=file_name)
    app.run()
    print("Time taken : ", time.time() - start)


if __name__ == "__main__":
    urls = input("Enter the URLs you want to download: \n").split(' ')
    for url in urls:
        name = input("Enter the name of file : \n")
        images = read_manga(url)
        download_manga(images, file_name=name)


