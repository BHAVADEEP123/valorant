import json
import os
import sys

# Get the path to the parent directory and add it to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from scrapy.crawler import CrawlerProcess
from player_scrapper.player_scrapper.spiders.player_info import PlayerSpider


def extract_links_from_json(team_data):
    """
    Extracts all 'player_link' values from a JSON object.

    Args:
        team_data (dict): A dictionary representing the JSON structure.

    Returns:
        str: A comma-separated string of all player links.
    """
    all_links = []

    if "players" in team_data and isinstance(team_data["players"], list):
        for player in team_data["players"]:
            if "player_link" in player:
                all_links.append(player["player_link"])


    # Join all collected links with a comma and return the string
    return all_links

if __name__ == "__main__":

    output_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(output_dir, 'data', 'top_level_data','roster.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            for data in json_data:
                if "teams" in data and isinstance(data["teams"], list):
                    for team in data["teams"]:
                        links = extract_links_from_json(team)
                        print(f"Found {len(links)} URLs to crawl.")
                        output_file_path = os.path.join(output_dir,'data','players_data',
                                                        f'{'_'.join(str(team["team_name"]).split()).lower()}.json')
                        settings = {
                            'FEEDS': {
                                output_file_path: {
                                    'format': 'json',
                                    'overwrite': True,
                                    'encoding': 'utf8',
                                },
                            },
                            'FEED_EXPORT_INDENT': 4,
                            'LOG_LEVEL': 'INFO'
                        }
                        process = CrawlerProcess(settings=settings)
                        process.crawl(PlayerSpider, start_urls=links)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    if process.crawlers:
        print("\nStarting the Scrapy process...")
        process.start()
        print("All crawls finished.")
    else:
        print("No crawls were scheduled.")
