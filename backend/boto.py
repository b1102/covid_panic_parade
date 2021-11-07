import dataclasses

import boto3
from bson import ObjectId

from backend.news.data_combiner import ChartItem

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my_table')

item = ChartItem(id=str(ObjectId()), date="today", mass_media_chart_position=2, country_name="popa",
                 fractions_of_covid_news=25, covid_stats_chart_position=2, week_deaths_per_million=6,
                 analyzed_news_entries_number=255, diff=2)
item = dataclasses.asdict(item)


table.put_item(
    Item=item
)
