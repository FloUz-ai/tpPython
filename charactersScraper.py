import scrapy


class charactersSpider(scrapy.Spider):
    name = 'characters'
    start_urls = [
        'https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation',
    ]

    def parse(self, response):
        for characters in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {
                   'character': characters.css('a ::text').get() }



