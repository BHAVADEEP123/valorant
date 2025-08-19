# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerItem(scrapy.Item):
    player_name = scrapy.Field()
    player_link = scrapy.Field()


class TeamItem(scrapy.Item):
    team_name = scrapy.Field()
    team_link = scrapy.Field()
    players = scrapy.Field()  # list of PlayerItem


class RegionItem(scrapy.Item):
    region = scrapy.Field()
    region_link = scrapy.Field()
    teams = scrapy.Field()  # list of TeamItem

