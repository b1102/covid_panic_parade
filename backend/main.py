import feedparser

from backend.covid_stats.generate_stats import stats
from backend.news.data_combiner import combine_data
from backend.news.rss_providers_addresses_reader import rss_addresses_per_country
from backend.news.utils import mentions

countries = rss_addresses_per_country()
mass_media_impact_index_per_country = {}

for country in countries:
    print("Started processing: {}".format(country))
    coronavirus_entries_counter = 0
    entries_counter = 0

    for address in countries.get(country):
        feed = feedparser.parse(address)
        for entry in feed.entries:
            entries_counter = entries_counter + 1
            coronavirus_entries_counter = coronavirus_entries_counter + mentions(entry)

    mass_media_impact_index = coronavirus_entries_counter / entries_counter
    mass_media_impact_index_per_country[country] = (mass_media_impact_index, entries_counter)
    print("Covid mass media impact index for {} is {}".format(country, mass_media_impact_index))
    print("Results are based on analyzing: {} news entries".format(entries_counter))
    print("Finished processing: {}".format(country))
    print()

data = combine_data(mass_media_impact_index_per_country, stats())

for entry in data:
    print(entry)
