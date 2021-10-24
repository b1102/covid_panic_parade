from dataclasses import dataclass
from typing import List


@dataclass
class ChartItem:
    mass_media_chart_position: int
    country_name: str
    fractions_of_covid_news: float
    covid_stats_chart_position: int
    week_deaths_per_million: float
    analyzed_news_entries_number: int


def combine_data(mass_media_impact_index, covid_stats) -> List[ChartItem]:
    toReturn = []
    for country in mass_media_impact_index:
        chartItem = ChartItem(
            mass_media_chart_position=list(mass_media_impact_index).index(country) + 1,
            country_name=country,
            fractions_of_covid_news=round(mass_media_impact_index[country][0] * 100, 1),
            covid_stats_chart_position=list(covid_stats).index(country) + 1,
            week_deaths_per_million=covid_stats[country],
            analyzed_news_entries_number=mass_media_impact_index[country][1]
        )
        toReturn.append(chartItem)
    return toReturn
