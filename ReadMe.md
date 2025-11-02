#  Wedding Spot Venues Scraper

This is a **Scrapy-based web scraper** designed to extract wedding venue information from [Wedding-Spot.com](https://www.wedding-spot.com/). The spider scrapes venues from various regions and collects details like venue name, phone number, guest capacity, venue highlights, and address.


##  Features

- Scrapes multiple pages using pagination
- Extracts these venue details:
  -  Venue name  
  -  Phone number  
  -  Guest capacity  
  -  Venue highlights  
  -  Full address
- Built with the **Scrapy framework**
- Customizable and easy to extend


### Setup a Virtual Environment (Optional but Recommended)

#### On macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate

### On Windows:
python -m venv venv
venv\Scripts\activate



## Installation

```bash
pip install -r requirements.txt

## how to Run
```bash
scrapy crawl wedding_spot_venues_scrapy -O venues.json

## output pattern 
'''bash
{
  "url": "https://www.wedding-spot.com/venue/12345/",
  "venue_name": "The Grand Ballroom",
  "phone": "(123) 456-7890",
  "venue_highlights": [
    "Indoor and outdoor spaces",
    "Valet parking",
    "Scenic views"
  ],
  "guest_capacity": "200",
  "address": "123 Wedding Lane, New Jersey, USA"
}


