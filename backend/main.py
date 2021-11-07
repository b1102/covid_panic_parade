import argparse
import logging

from backend.common.s3 import fetch_s3_data
from backend.news.data_fetcher import fetch_new_data

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry_run', type=bool)
    args = parser.parse_args()

    if args.dry_run:
        data = fetch_s3_data()
    else:
        data = fetch_new_data()

    for entry in data:
        logging.info(entry)


if __name__ == '__main__':
    main()
