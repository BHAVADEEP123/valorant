import scrapy

class RoasterSpider(scrapy.Spider):
    name = "roaster-test"
    start_urls = ["https://www.vlr.gg/team/624/paper-rex"]

    def parse(self, response):
        team_name = response.css("h1::text").get().strip()
        yield {"team_name": team_name}
        # Example: scrape roster players
        for player in response.css(".team-roster-item"):
            # ign = player.css("div.team-roster-item-name-alias::text").get().strip()
            # ign = player.xpath("div[@class='team-roster-item-name-alias']/text()").get()
            # if ign:
            #     ign = ign.strip()
            ign = player.css("div.team-roster-item-name-alias::text").getall()
            ign = "".join([i.strip() for i in ign if i.strip()])

            real_name = player.css(".team-roster-item-name-real::text").get().strip()
            yield {
                "ign": ign,
                "real_name": real_name
            }
