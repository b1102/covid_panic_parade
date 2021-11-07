import logging

import feedparser

from backend.common.s3 import write_to_s3
from backend.covid_stats.generate_stats import stats
from backend.news.data_combiner import combine_data
from backend.news.mentions.rss_providers_addresses_reader import rss_addresses_per_country
from backend.news.mentions import mentions


def fetch_new_data():
    countries = rss_addresses_per_country()
    mass_media_impact_index_per_country = {}
    for country in countries:
        logging.info("Started processing: {}".format(country))
        coronavirus_entries_counter = 0
        entries_counter = 0

        for address in countries.get(country):
            feed = feedparser.parse(address)
            for entry in feed.entries:
                entries_counter = entries_counter + 1
                coronavirus_entries_counter = coronavirus_entries_counter + mentions(entry)

        mass_media_impact_index = coronavirus_entries_counter / entries_counter
        mass_media_impact_index_per_country[country] = (mass_media_impact_index, entries_counter)
        logging.info("Covid mass media impact index for {} is {}".format(country, mass_media_impact_index))
        logging.info("Results are based on analyzing: {} news entries".format(entries_counter))
        logging.info("Finished processing: {}".format(country))
        logging.info('_________________________________________________________________________________')
    data = combine_data(mass_media_impact_index_per_country, stats())
    write_to_s3(data)
    return data
