# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerScrapperItem(scrapy.Item):
    player_name = scrapy.Field()
    player_id = scrapy.Field()
    agent_data = scrapy.Field()

class AgentItem (scrapy.Item):
    agent_name = scrapy.Field()
    times_played = scrapy.Field()
    rounds_played = scrapy.Field()
    rating = scrapy.Field()
    acs = scrapy.Field()
    kd = scrapy.Field()
    adr = scrapy.Field()
    kast = scrapy.Field()
    kpr = scrapy.Field()
    apr = scrapy.Field()
    fkpr = scrapy.Field()
    fdpr = scrapy.Field()
    kills = scrapy.Field()
    deaths = scrapy.Field()
    assists = scrapy.Field()
    first_bloods = scrapy.Field()
    first_deaths = scrapy.Field()