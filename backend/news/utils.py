from backend.news.covid_words_reader import covid_words


def mentions(summary: str):
    # todo: title, description
    for word in covid_words():
        if word in summary:
            return 1
    return 0
