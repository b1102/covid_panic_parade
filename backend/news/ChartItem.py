from dataclasses import dataclass


@dataclass
class ChartItem:
    mass_media_chart_position: int
    country_name: str
    fractions_of_covid_news: float
    covid_stats_chart_position: int
    week_deaths_per_million: float
    analyzed_news_entries_number: int
    diff: int
