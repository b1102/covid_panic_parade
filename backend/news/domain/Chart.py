from dataclasses import dataclass
from typing import List

from backend.news.domain.ChartItem import ChartItem


@dataclass
class Chart:
    id: str
    date: str
    chart: List[ChartItem]
