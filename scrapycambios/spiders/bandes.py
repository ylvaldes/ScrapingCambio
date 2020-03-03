# -*- coding: utf-8 -*-
import scrapy


class BandesSpider(scrapy.Spider):
    name = 'bandes'
    allowed_domains = ['www.bandes.com.uy']
    start_urls = ['http://www.bandes.com.uy/']

    def parse(self, response):
        for divisa in response.css(".cotizaciones tbody tr"):
            yield {
                "Name":divisa.css("td:nth-child(1)::text").extract_first(),
                "Compra":divisa.css("td:nth-child(2)::text").extract_first(),
                "Venta":divisa.css("td:nth-child(3)::text").extract_first()
            }