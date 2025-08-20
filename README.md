# valorant
Creating a repository for analysing valorant players patterns
   
## Setup
```commandline
uv sync
```
## Run Roaster spider
From roaster_scrapper folder
```commandline
 uv run scrapy crawl roaster -O ../data/top_level_data/roster.json --set FEED_EXPORT_INDENT=4
```

## Run Player Individual Data Spider
From main directory
```commandline
 uv run python scripts/populate_players_data.py
```