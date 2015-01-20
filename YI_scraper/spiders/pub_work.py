# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request
from urlparse import urljoin
import YI_scraper.items as itm

class PubWorkSpider(scrapy.Spider):
    name = "pub_work"
    allowed_domains = ["contratos.gov.co"]
    results_per_page = '10000' # high enough to fit every record in one request
    # 'http://www.contratos.gov.co/consultas/inicioConsulta.do',
    start_urls =  (
        'http://www.contratos.gov.co/consultas/resultadosConsulta.do?'\
        '&entidad=&departamento=&paginaObjetivo=1&fechaInicial=&desdeFomulario=true' \
        '&registrosXPagina='+results_per_page+'' \
        '&estado=0&cuantia=0&fechaFinal=' \
        '&objeto=95000000' # 'Terrenos, Edificios, Estructuras y Vías' \
        '&tipoProceso=1' # 'licitacion publica' \-
        '&numeroProceso=&municipio=0',
    )

    def parse(self, response):
        # "javascript: popUpSecop('/consultas/detalleProceso.do?numConstancia=14-1-123441')"
        links = response.css('a.link_azul::attr(href)').re(r'\(\'(.*)\'\)')
        return (Request(urljoin(response.url, url), callback=self.parse_contract) for url in links)

    def parse_contract(self, res):
        contract = itm.PublicWorkItem()
        contract['organization'] = res.css('.subtitulos::text').extract()
        # contract['name'] = res.xpath('').extract()
        contract['description'] = res.css('.tablaslistOdd textarea::text').extract()
        # contract['price'] = res.xpath('').extract()
        # contract['process'] = res.xpath('').extract()
        # contract['location'] = res.xpath('').extract()
        # contract['start_date'] = res.xpath('').extract()
        # contract['end_date'] = res.xpath('').extract()
        return contract