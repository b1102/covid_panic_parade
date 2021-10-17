import yaml


def sort_mass_media_impact_index(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1][0], reverse=reverse))


def sort_covid_stats(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def read_yaml(path):
    with open(path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None
