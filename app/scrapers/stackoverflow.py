from __future__ import print_function
from generalized import Scraper


class StackOverflow(Scraper):
    """Scrapper class for StackOverflow"""

    def __init__(self):
        self.url = 'https://stackoverflow.com/search'
        self.result_url = 'https://stackoverflow.com'

    def parseResponse(self, soup):
        """ Parse the response and return set of urls
        Returns: urls (list)
                [[Tile1,url1], [Title2, url2],..]
        """
        urls = []
        for div in soup.findAll('div', {'class': 'result-link'}):
            a = div.find('a')
            link = self.result_url + str(a.get('href'))
            urls.append({
                    'title': a.getText().strip(),
                    'link': link
                })
        print('StackOverflow parsed: ' + str(urls))

        return urls
