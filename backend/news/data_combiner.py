from typing import List

from backend.common.utils import sort_mass_media_impact_index, sort_covid_stats
from backend.news.ChartItem import ChartItem


def combine_data(mass_media_impact_index_per_country, covid_stats) -> List[ChartItem]:
    mass_media_impact_index = sort_mass_media_impact_index(mass_media_impact_index_per_country, True)
    covid_stats = needed_stats(covid_stats, mass_media_impact_index)

    toReturn = []
    for country in mass_media_impact_index:
        chartItem = ChartItem(
            mass_media_chart_position=list(mass_media_impact_index).index(country) + 1,
            country_name=country,
            fractions_of_covid_news=round(mass_media_impact_index[country][0] * 100, 1),
            covid_stats_chart_position=list(covid_stats).index(country) + 1,
            week_deaths_per_million=covid_stats[country],
            analyzed_news_entries_number=mass_media_impact_index[country][1],
            diff=list(mass_media_impact_index).index(country) - list(covid_stats).index(country)
        )
        toReturn.append(chartItem)
    return toReturn


def needed_stats(covid_stats, mass_media_impact_index):
    covid_stats_used = {}
    for country in mass_media_impact_index:
        covid_stats_used[country] = covid_stats[country]
    covid_stats_used = sort_covid_stats(covid_stats_used, True)
    return covid_stats_used
