from comic_reader import Founder, Downloader


def read_manga():
    url = input("Enter the URL you want to download: \n")
    app = Founder(url)
    app.search_html(tage="img")
    links = app.get_link()
    return links


def download_manga(thelist):
    path = input("Enter the name of file : \n")
    app = Downloader()
    app.set(images=thelist, save_as=path)
    app.run()


if __name__ == "__main__":
    images = read_manga()
    download_manga(images)
