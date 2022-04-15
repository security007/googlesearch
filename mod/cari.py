import requests
from bs4 import BeautifulSoup as bs


class Search:
    def __init__(self, query, limit=10, domain=False, save=None):
        self.query = query
        self.limit = limit
        self.domain = domain
        self.save = save
        self.head = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        self.url = 'https://www.google.com/search?q='
        self.results = list()

    def get_domain(self, url):
        return url.split("/")[0]+"//"+url.split("/")[2]+"/"

    def get_results(self):
        if self.limit == 10:
            r = requests.get(self.url+self.query, headers=self.head)
            beauty = bs(r.text, 'html.parser')

            if "Penelusuran Google" in beauty.title.text:
                get_link = beauty.find_all('div', {'class': 'yuRUbf'})
                for link in get_link:
                    if self.domain:
                        self.results.append(self.get_domain(
                            link.find('a').get('href')))
                    else:
                        self.results.append(link.find('a').get('href'))
                if self.save != None:
                    buka = open("results/"+self.save, "a")
                    for res in self.results:
                        buka.write(res+"\n")
            else:
                self.results.append(0)
        else:
            for x in range(0, self.limit, 10):
                r = requests.get(self.url+self.query +
                                 "&start="+str(x), headers=self.head)
                beauty = bs(r.text, 'html.parser')

                if "Penelusuran Google" in beauty.title.text:
                    get_link = beauty.find_all('div', {'class': 'yuRUbf'})
                    for link in get_link:
                        if self.domain:
                            self.results.append(self.get_domain(
                                link.find('a').get('href')))
                        else:
                            self.results.append(link.find('a').get('href'))
                    if self.save != None:
                        buka = open("results/"+self.save, "a")
                        for res in self.results:
                            buka.write(res+"\n")
                else:
                    self.results.append(0)
        # return self.results
        if len(self.results) != 0:
            if self.results[0] != 0:
                return self.results
            else:
                return ["Captcha blocked"]
        else:
            return ["No results"]
