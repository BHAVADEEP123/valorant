import scrapy
from ..items import AgentItem, PlayerScrapperItem

class PlayerSpider(scrapy.Spider):
    name = "player"

    def __init__(self, start_urls=None, *args, **kwargs):
        super(PlayerSpider, self).__init__(*args, **kwargs)
        if start_urls:
            self.start_urls = start_urls
        else:
            self.start_urls = ["https://www.vlr.gg/player/1916/free1ng?timespan=all"]


    def parse(self, response):
        player_name = response.url.split("/")[-1]
        player_id = response.url.split("/")[-2]
        agents = []
        for row in response.css('tbody tr'):
            agent_item = AgentItem()
            agent_item['agent_name'] = row.css('td:nth-child(1) img::attr(alt)').get().strip()
            agent_item['times_played'] = row.css('td:nth-child(2) span::text').get().split()[1].strip()
            agent_item['rounds_played'] = row.css('td:nth-child(3)::text').get().strip()
            agent_item['rating'] = row.css('td:nth-child(4)::text').get().strip()
            agent_item['acs'] = row.css('td:nth-child(5)::text').get().strip()
            agent_item['kd'] = row.css('td:nth-child(6)::text').get().strip()
            agent_item['adr'] = row.css('td:nth-child(7)::text').get().strip()
            agent_item['kast'] = row.css('td:nth-child(8)::text').get().strip()
            agent_item['kpr'] = row.css('td:nth-child(9)::text').get().strip()
            agent_item['apr'] = row.css('td:nth-child(10)::text').get().strip()
            agent_item['fkpr'] = row.css('td:nth-child(11)::text').get().strip()
            agent_item['fdpr'] = row.css('td:nth-child(12)::text').get().strip()
            agent_item['kills'] = row.css('td:nth-child(13)::text').get().strip()
            agent_item['deaths'] = row.css('td:nth-child(14)::text').get().strip()
            agent_item['assists'] = row.css('td:nth-child(15)::text').get().strip()
            agent_item['first_bloods'] = row.css('td:nth-child(16)::text').get().strip()
            agent_item['first_deaths'] = row.css('td:nth-child(17)::text').get().strip()

            agents.append(agent_item)

        yield {
            "player_name": player_name,
            "player_id": player_id,
            "agents": agents,
        }
