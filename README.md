# Amazon-Review-Scraper
Scraps amazon reviews provided a list of product_urls using scrapy framework and pipelines output to MySQLdb


To pipeline the output to the csv file:
```
scrapy crawl amazon -t csv -o yourfilename.csv
```

Arguments:
 * `-L` to set logging level (e.g. INFO)

## Mysql
To pipeline the output to MySQL Server, go to `reviews/pipelines.py `and update your *username, password* of your MySQL Server and *db name* . And then go to go to `reviews/settings.py` and uncomment these lines:

```
ITEM_PIPELINES = [
  'reviews.pipelines.MySQLStorePipeline',
]
```

```
scrapy crawl amazon
```

I used the following SQL-schema:

```
CREATE TABLE `reviews` (
  `review_id` text NOT NULL,
  `asin` text,
  `author_id` text,
  `author_link` text,
  `author_name` text,
  `review_link` text,
  `total_reviews_count` text,
  `review_date` text,
  `title` text,
  `ratings` text,
  `helpful_votes` text,
  `total_votes` text,
  `verified` text,
  `comments_count` text,
  `images_count` text,
  `has_video` tinyint(1) DEFAULT NULL,
  `text` text,
  `updated` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

# References
Scrapy framework [Documentation](http://scrapy.org/doc/)
