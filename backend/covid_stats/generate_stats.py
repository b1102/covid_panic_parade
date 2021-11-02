import requests
from bs4 import BeautifulSoup


def stats():
    request = requests.get('https://www.worldometers.info/coronavirus/weekly-trends/#weekly_table')
    soup = BeautifulSoup(request.content, 'html.parser')
    table = soup.find("table", id="main_table_countries_today")
    lines = table.find_all('tr')

    stats = {}
    for i in range(8, 211):
        line = lines[i]
        country = country_name(line)
        weekly_deaths_per_million = float(line.find_all('td')[9].contents[0])
        stats[country] = weekly_deaths_per_million

    return stats


def country_name(line):
    names_mapping = {"usa": "united states", "uk": "united kingdom", "s. korea": "south korea"}
    country_name = line.find_all('td')[1].find('a').contents[0].lower()
    if country_name in names_mapping:
        return names_mapping[country_name]
    else:
        return country_name
