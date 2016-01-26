# Amazon-Review-Scraper
Scraps amazon reviews provided a list of product_urls using scrapy framework and pipelines output to MySQLdb



> **Execution** 
 - To pipeline the output to the csv file:
	`scrapy crawl -t csv -o yourfilename.csv `
- To pipeline the output to MySQL Server, go to `reviews/pipelines.py `and update your *username, password* of your MySQL Server and *db name* . And then go to go to `reviews/settings.py` and uncomment these lines:

      ITEM_PIPELINES = [
         'reviews.pipelines.MySQLStorePipeline',
         ]


# References
Scrapy framework [Documentation](http://scrapy.org/doc/)
