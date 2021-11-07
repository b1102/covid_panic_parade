import io
import logging
import sys
from datetime import datetime

import boto3
from botocore.exceptions import ClientError
from bson import ObjectId
import ruamel.yaml

from backend.news.Chart import Chart
from backend.news.data_combiner import ChartItem
#
# yaml = ruamel.yaml.YAML()
# yaml.register_class(ChartItem)
# yaml.register_class(Chart)
#
# s3 = boto3.resource('s3')
#
# today = datetime.today()
# date = today.strftime('%Y-%m-%d')
#
# id = str(ObjectId())
# history = s3.Object('covid-panic-parade',
#                     '/chart/{}/{}/{}/{}.yaml'
#                     .format(
#                         today.strftime('%Y'),
#                         today.strftime('%m'),
#                         today.strftime('%d'),
#                         id
#                     ))
#
# item = ChartItem(mass_media_chart_position=2, country_name="popa",
#                  fractions_of_covid_news=25, covid_stats_chart_position=2, week_deaths_per_million=6,
#                  analyzed_news_entries_number=255, diff=2)
#
# chart = Chart(id=id, date=date, chart=[item])
#
# buf = io.BytesIO()
# yaml.dump(chart, buf)
#
# result = history.put(Body=buf.getvalue())
#
# # print(object.get()['Body'].read().decode('utf-8'))
#
# # load = yaml.load(object.get()['Body'].read().decode('utf-8'))
#
# print(date)
logging.info("Starting to write data to s3")
