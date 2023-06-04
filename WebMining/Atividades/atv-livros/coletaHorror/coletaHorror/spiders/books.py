import scrapy
import re


class BooksSpider(scrapy.Spider):
    name = "books"
    #allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/horror_31/index.html"]

    def parse(self, response):
        titulos = response.css('h3 a::text').getall()
        preco = response.css('.price_color::text').getall()
        estoque = response.css('.availability::text').getall()
        
        for books in response.css('.col-lg-3'):
            yield{
                'titulo': books.css('h3 a::text').get(),
                'preco': books.css('.price_color::text').get(),
                'estoque': re.sub("(^[\n\s]*)|([\n\s]*$)", "", books.css('.availability::text').getall()[1]),
            }
        #dict ={
            #"titulos":titulos,
            #"preco":preco,
            #"estoque":estoque
        #}
        pass
        #return dict
