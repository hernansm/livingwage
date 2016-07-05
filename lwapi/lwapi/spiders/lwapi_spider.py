import scrapy

class DmozSpider(scrapy.Spider):
    name = "lwapi"
    allowed_domains = ["livingwage.mid.edu"]
    start_urls = [
        "http://livingwage.mit.edu/states/01/"
        ]

    def parse(self, response):
        locationId = 
        location = response.xpath("/html/body/div[@class='container']" +
                    "/div[@class='content']/h1/text()").extract()
        livingWage = response.xpath("/html/body/div[@class='container']" +
                    "/div[@class='table-responsive']/table/tbody/tr/").extract()
        povertyWage = 
        minimumWage = 
        print title