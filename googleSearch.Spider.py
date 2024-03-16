import scrapy

class GoogleSearchSpider(scrapy.Spider):
    name = 'google_search'
    start_urls = ['https://www.google.com/search?q=electronics']

    def parse(self, response):
        # Extract search result titles, URLs, and descriptions
        search_results = response.css('div.g')
        for result in search_results:
            title = result.css('h3::text').get()
            url = result.css('a::attr(href)').get()
            description = result.css('span.st::text').get()
            yield {
                'title': title,
                'url': url,
                'description': description
            }

        # Follow pagination links if needed
        next_page = response.css('a.pn::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
