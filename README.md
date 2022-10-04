Find and extract all not found(404) pages of a website.

# Requirements

- Python
- Scrapy

# Usage

Configure urls to parse. Then, run:

<code>scrapy runspider broken_links_spider.py -o output.json</code>

## Output
Then check 404 items in the output.json file.
