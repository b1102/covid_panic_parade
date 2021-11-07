from backend.common.utils import read_yaml


def covid_words():
    return set(read_yaml("./news/resourses/covid_words.yaml").split())