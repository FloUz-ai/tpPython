import scrapy

urlList = []

for i in range (287):
    urlList.append ("http://www.linternaute.fr/citation/meilleures_citations/{}/".format(i+1))

class charactersSpider(scrapy.Spider):
    name = 'quotes'
    start_urls =  urlList

    def parse(self, response):
        for title in response.css('div.layout_main tr td.libelle_citation'):
            yield {'quote': title.css('a ::text').get()}
