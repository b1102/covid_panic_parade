import logging

import requests
from bs4 import BeautifulSoup


def stats():
    logging.info("Getting covid deaths stats")
    request = requests.get('https://www.worldometers.info/coronavirus/weekly-trends/#weekly_table')
    soup = BeautifulSoup(request.content, 'html.parser')
    table = soup.find("table", id="main_table_countries_today")
    lines = table.find_all('tr')

    stats = {}
    for line in lines:
        country, weekly_deaths_per_million = country_deaths(line)
        stats[country] = weekly_deaths_per_million

    logging.info("Covid deaths stats fetched")
    return stats


def country_deaths(line):
    names_mapping = {"usa": "united states", "uk": "united kingdom", "s. korea": "south korea"}
    found = line.find_all('td')[1].find('a')
    if found:
        country_name = found.contents[0].lower()
        value = float(line.find_all('td')[9].contents[0])
        if country_name in names_mapping:
            return names_mapping[country_name], value
        else:
            return country_name, value
    return "", 0.0
