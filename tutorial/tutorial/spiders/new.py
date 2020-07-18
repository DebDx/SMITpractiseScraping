import scrapy
import re
class scrapespider(scrapy.Spider):
    name="scrapp"
    start_urls=['https://results.smu.edu.in/smit/results_grade_view.php?exam=45&subject=10931']
    def parse(self, response):
        a=response.css(".content::text").extract()
        for b in a:
            regex=re.compile(r'[\n\r\t\xa0]')
            b=regex.sub(" ", b)
            s=b.split()
            try:
                if re.match("^20*",s[0]) is not None:
                    yield{'reg no': s[0],
            'internal': s[1],
            'external':s[2],
            'overall':s[3],
            'grade':s[4]}
            except IndexError:
                continue