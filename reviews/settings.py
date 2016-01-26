# -*- coding: utf-8 -*-

BOT_NAME = 'reviews'

SPIDER_MODULES = ['reviews.spiders']
NEWSPIDER_MODULE = 'reviews.spiders'
DEFAULT_ITEM_CLASS = 'reviews.items.ReviewsItem'

# If you want to pipeline the output of the spider to MySQLDb server, uncomment the following lines
# and enter credentials of the server in reviews/pipelines.py
# ITEM_PIPELINES = [
#      'reviews.pipelines.MySQLStorePipeline',
# ]

DOWNLOAD_HANDLERS = {
  's3': None,
}
