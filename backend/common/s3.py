import io
import logging
from typing import List

from ruamel import yaml

from backend.news.Chart import Chart
from datetime import datetime

import boto3
from bson import ObjectId
import ruamel.yaml

from backend.news.ChartItem import ChartItem


def write_to_s3(list: List[ChartItem]):
    yaml = ruamel.yaml.YAML()
    yaml.register_class(ChartItem)
    yaml.register_class(Chart)

    today = datetime.today()
    id = str(ObjectId())
    chart = Chart(id, today.strftime('%Y-%m-%d'), list)

    logging.info("Starting to write data to s3")
    write_history(today, yaml, chart)
    write_latest(yaml, chart)
    logging.info("Data was written to s3")


def write_history(today, yaml, chart):
    s3 = boto3.resource('s3').Object(
        'covid-panic-parade',
        '/chart/{}/{}/{}/{}.yaml'
            .format(
            today.strftime('%Y'),
            today.strftime('%m'),
            today.strftime('%d'),
            chart.id)
    )

    buf = io.BytesIO()
    yaml.dump(chart, buf)

    s3.put(Body=buf.getvalue())


def write_latest(yaml, chart):
    s3 = boto3.resource('s3').Object(
        'covid-panic-parade', '/chart/latest/latest.yaml'
    )

    buf = io.BytesIO()
    yaml.dump(chart, buf)

    s3.put(Body=buf.getvalue())
