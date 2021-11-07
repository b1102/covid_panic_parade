from backend.news.mentions.covid_words_reader import covid_words


def mentions(entry):
    if "title" in entry:
        title = entry.get("title").lower()
        for word in covid_words():
            if word in title:
                return 1
    if "description" in entry:
        description = entry.get("description").lower()
        for word in covid_words():
            if word in description:
                return 1
    if "summary" in entry:
        summary = entry.get("summary").lower()
        for word in covid_words():
            if word in summary:
                return 1
    return 0
