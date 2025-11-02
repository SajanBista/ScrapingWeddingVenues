# wedding_scraper/spiders/venues_spider_scrapy_only.py
import scrapy
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

class WeddingSpotVenueItem(scrapy.Item):
    url = scrapy.Field()
    venue_name = scrapy.Field()
    phone = scrapy.Field()
    venue_highlights = scrapy.Field()
    guest_capacity = scrapy.Field()
    address = scrapy.Field()

class VenuesSpider(scrapy.Spider):
    name = 'wedding_spot_venues_scrapy'
    start_urls = [
        'https://www.wedding-spot.com/wedding-venues/?pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1'
    ]
    
    current_page = 1

    def parse(self, response):
        self.log(f"Processing listing page: {response.url}")

        venue_links = response.xpath('//a[starts-with(@href, "/venue/")]/@href').getall()
        for link in venue_links:
            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_details
            )

        # Pagination
        next_page_enabled = response.xpath('//button[@aria-label="Next Page" and not(@disabled)]').get()
        if next_page_enabled:
            self.current_page += 1
            parsed_url = urlparse(response.url)
            query_params = parse_qs(parsed_url.query)
            query_params['page'] = [str(self.current_page)]
            next_query = urlencode(query_params, doseq=True)
            next_page_url = urlunparse(parsed_url._replace(query=next_query))
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        item = WeddingSpotVenueItem()
        item['url'] = response.url

        # Venue Name
        item['venue_name'] = response.css('h1::text').get()

        # Phone
        # item['phone'] = response.xpath("//a[contains(@href,'tel:')]/text()").get()
        item["phone"] = response.xpath("//a[contains(@href, 'tel:')]//text()").get() #confirmed through shell

        # Venue Highlights
        highlights = response.xpath("//div[contains(@class,'VenueHighlights')]//text()").getall()
        item['venue_highlights'] = [x.strip() for x in highlights if x.strip()]

        # Guest Capacity
        guest_capacity = response.xpath("//h3[text()='Guest capacity:']/following-sibling::p//text()").get()
        if guest_capacity:
            import re
            match = re.search(r'\d+', guest_capacity)
            item['guest_capacity'] = match.group() if match else guest_capacity

        # Address
        address = response.xpath("//h3[text()='Location:']/following-sibling::p//text()").getall()
        item['address'] = " ".join([x.strip() for x in address if x.strip()]) if address else None

        yield item
