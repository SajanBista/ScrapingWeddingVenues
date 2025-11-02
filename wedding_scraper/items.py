import scrapy

class WeddingSpotVenueItem(scrapy.Item):
    # A - Url (url of the detail page)
    url = scrapy.Field()
    # B - Venue Name
    venue_name = scrapy.Field()
    # C - Phone
    phone = scrapy.Field()
    # D - Venue Highlights
    venue_highlights = scrapy.Field()
    # E - Guest Capacity
    guest_capacity = scrapy.Field()
    # F - Address
    address = scrapy.Field()