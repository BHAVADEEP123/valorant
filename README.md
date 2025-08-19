# valorant
Creating a repository for analysing valorant players patterns
   
## Setup
```commandline
uv sync
```
## Run a spider
```commandline
uv run scrapy crawl roaster -O roster.json --set FEED_EXPORT_INDENT=4
```