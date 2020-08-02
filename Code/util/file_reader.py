from typing import Dict

import pandas as pd

# TODO move names to config?
file_path = '../Resources/processed_reviews.tsv'
date_name = 'Date'


def get_reviews_df(start_date: str, end_date: str) -> pd.DataFrame:
    # TODO cache reviews
    reviews = pd.read_csv(file_path, sep='\t')
    # To include all times
    end_date = end_date + "Z"
    reviews = reviews[reviews[date_name].between(start_date, end_date)]
    return reviews


def get_json(start_date, end_date):
    return get_reviews_df(start_date, end_date).to_json(force_ascii=False, orient='records')


def get_csv(start_date, end_date):
    # TODO fix possible memory error
    return get_reviews_df(start_date, end_date).to_csv(sep='\t')


def get_type_counts(start_date, end_date) -> Dict[str, int]:
    return get_reviews_df(start_date, end_date).groupby('Intention').count()['Link'].to_dict()
