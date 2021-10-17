from backend.common.utils import read_yaml


def covid_stats():
    return read_yaml("./covid_stats/stats.yaml")
