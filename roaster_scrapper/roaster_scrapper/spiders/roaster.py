import scrapy
from ..items import RegionItem, TeamItem, PlayerItem

class RoasterSpider(scrapy.Spider):
    name = "roaster"
    start_urls = ["https://www.vlr.gg/event/2500/vct-2025-pacific-stage-2", "https://www.vlr.gg/event/2380/vct-2025-emea-stage-1", "https://www.vlr.gg/event/2499/vct-2025-china-stage-2", "https://www.vlr.gg/event/2347/vct-2025-americas-stage-1"]

    def parse(self, response):
        region_name = response.css("h1::text").get().strip()
        region_item = RegionItem()
        region_item["region"] = region_name
        region_item["region_link"] = response.url
        region_item["teams"] = []
        for team in response.css("div.wf-card.event-team"):
            team_item = TeamItem()
            team_item["team_name"] = team.css("a.event-team-name::text").get().strip()
            team_item["team_link"] = team.css("a.event-team-name::attr(href)").get().strip()
            team_item["team_id"] = team.css("a.event-team-name::attr(href)").get().strip().split("/")[-2]
            team_item["players"] = []
            for player in team.css("a.event-team-players-item"):
                player_item = PlayerItem()
                player_item["player_name"] = "".join(
                    [i.strip() for i in player.css("::text").getall() if i.strip()]
                )
                player_item["player_link"] = response.urljoin(player.attrib["href"])
                player_item["player_id"] = player.attrib["href"].split("/")[-2]
                team_item["players"].append(player_item)

            region_item["teams"].append(team_item)
        print(region_item)
        yield region_item