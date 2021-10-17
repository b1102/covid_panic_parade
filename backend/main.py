import feedparser

from backend.common.utils import sort_mass_media_impact_index, sort_covid_stats
from backend.covid_stats.covid_stats_reader import covid_stats
from backend.news.data_combiner import combine_data
from backend.news.rss_providers_addresses_reader import rss_addresses_per_country

countries = rss_addresses_per_country()
mass_media_impact_index_per_country = {}

for country in countries:
    print("Started processing: {}".format(country))
    coronavirus_entries_counter = 0
    entries_counter = 0

    for address in countries.get(country):
        feed = feedparser.parse(address)
        for entry in feed.entries:
            # title, description
            if "summary" in entry:
                entries_counter = entries_counter + 1
                summary = entry.get("summary").lower()
                if "covid" in summary \
                        or "sars" in summary \
                        or "corona" in summary \
                        or "корона" in summary \
                        or "コロナ" in summary \
                        or "简体中文" in summary \
                        or "新冠病毒" in summary \
                        or "日本語" in summary \
                        or "繁體中文" in summary \
                        or "新型肺炎" in summary:
                    coronavirus_entries_counter = coronavirus_entries_counter + 1

    if entries_counter == 0:
        raise ValueError('Feed address {}, provides zero entries'.format(countries.get(country)))

    mass_media_impact_index = coronavirus_entries_counter / entries_counter
    mass_media_impact_index_per_country[country] = (mass_media_impact_index, entries_counter)
    print("Covid mass media impact index for {} is {}".format(country, mass_media_impact_index))
    print("Results are based on analyzing: {} news entries".format(entries_counter))
    print("Finished processing: {}".format(country))
    print()

mass_media_impact_index = sort_mass_media_impact_index(mass_media_impact_index_per_country, True)
covid_stats = sort_covid_stats(covid_stats(), True)
data = combine_data(mass_media_impact_index, covid_stats)

for entry in data:
    print(entry)
