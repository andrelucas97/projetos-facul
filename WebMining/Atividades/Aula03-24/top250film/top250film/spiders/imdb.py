import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    # allowed_domains = ["imdb.com"]
    start_urls = ["http://imdb.com/chart/top/"]

    def parse(self, response):
        titulos = response.css('.titleColumn a::text').getall()
        anos = response.css('.secondaryInfo::text').getall()
        notas = response.css('strong::text').getall()

        dict = {
            "titulos": titulos,
            "anos": anos,
            "notas":notas
        }
        pass
        return dict 
