import os
from bs4 import BeautifulSoup
import asyncio
import sys
import httpx


def get_url(url):  # get url and check the status if True return response
    response = httpx.get(url)
    if response.status_code == 200:
        return response
    else:
        print("Something went wrong.\nPlease try again.")


def animated(counter0, total_presses):
    sys.stdout.write('\r')  # Move the cursor back to the beginning of the line
    sys.stdout.write(
        f"Progress: [{'#' * counter0}{' ' * (total_presses - counter0)}] {counter0}/{total_presses}")
    sys.stdout.flush()  # these 3 lines give us a little better look by animated download line


class Founder(object):  # a class for get html and work with urls of tags
    def __init__(self, url):
        self.final_destination = None  # where we download our files
        self.downloads_space = None  #
        self.response = get_url(url)  # page url

    def search_html(self, tage=None):  # look for some stuff in html

        soup = BeautifulSoup(self.response.content, "html.parser")
        self.downloads_space = soup.select(tage)

    def get_link(self) -> list[str]:  # this function make us be able to work with  urls more
        print(f'{len(self.downloads_space)} available images . . .')
        print('STAR DOWNLOADING LINKS ...  \n')
        print('DONE')
        links = [link['src'] for link in self.downloads_space]
        return links


class Downloader(object):
    def __init__(self):
        self.name = None
        self.mylist = None
        self.path = os.getcwd()

    def set(self, images: list[str], save_as: str = None) -> None:  # set fundamental needs
        self.path = os.getcwd() + "/" + save_as  # where client need file
        self.mylist = images
        if not os.path.exists(self.path):  # if file not exist create it
            os.makedirs(os.getcwd() + "/" + save_as)

    def save(self, image: any, num: int = 0) -> None:  # save images
        # take path of web browser if path is None
        try:
            with open(f'{self.path}/{num}.png', mode='wb') as f:
                f.write(image)
        except FileNotFoundError:  # if file can't found
            print('File not found')
            sys.exit()

    async def download_images(self, url: str, num: int) -> None:
        async with httpx.AsyncClient() as session:
            try:  # for when one of pictures not working
                response = await session.get(url, timeout=10)
                assert response.status_code == 200
            except AssertionError:
                print(f'status : {response.status_code}')
                if 'y' in input(
                        'Do you want to download continue ? [Y/n] ').lower():  # if client let the presses continue
                    pass
                else:  # else exit
                    sys.exit('Exiting')
            content = response.content
            self.save(content, num)

    async def download(self) -> None:
        tasks = [self.download_images(image, num) for num, image in enumerate(self.mylist)]
        await asyncio.gather(*tasks)

    def run(self) -> None:  # run the program
        try:
            asyncio.run(self.download())
        except KeyboardInterrupt:
            print('Exiting')


if __name__ == '__main__':
    emoji = "\U0001f600"
    print('this app make sure you have easy time to read your comics', emoji)
