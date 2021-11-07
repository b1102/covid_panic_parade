from dataclasses import dataclass
from typing import List

from backend.news.ChartItem import ChartItem


@dataclass
class Chart:
    id: str
    date: str
    chart: List[ChartItem]
