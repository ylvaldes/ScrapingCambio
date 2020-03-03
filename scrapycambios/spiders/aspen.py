# -*- coding: utf-8 -*-
import scrapy


class AspenSpider(scrapy.Spider):
    name = 'aspen'
    allowed_domains = ['www.aspen.com.uy/sitio/']
    start_urls = ['http://www.aspen.com.uy/sitio/']

    def parse(self, response):
        for divisa in response.css(".md-divisas table tr.bd"):
            yield {
                "Name":divisa.css(".moneda.fixphone strong::text").extract_first(),
                "Compra":divisa.css("td:nth-child(2)::text").extract_first(),
                "Venta":divisa.css("td:nth-child(3)::text").extract_first()
            }