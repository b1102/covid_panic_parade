from backend.common.utils import read_yaml


def rss_addresses(country):
    return read_yaml("./news/resourses/country.yaml").get(country)


def rss_addresses_per_country():
    return read_yaml("./news/resourses/rss_providers.yaml")
