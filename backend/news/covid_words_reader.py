from backend.common.utils import read_yaml


def covid_words():
    return set(read_yaml("./news/covid_words.yaml").split())
