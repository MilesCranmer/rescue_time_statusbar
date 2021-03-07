# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from datetime import date, timedelta as td
from download import fname
import pandas as pd
import numpy as np


# %%
def load_data(cdate):
    return pd.read_csv(fname(cdate), sep='\t')


# %%
def load_data_week(cdate):
    return [load_data(date.today() - td(days=i)) for i in range(7, -1, -1)]


# %%
def score_day(cdate):
    df = load_data(cdate)
    score = np.sum((df.Productivity + 2) * df.Seconds) / (4 * np.sum(df.Seconds))
    return score*100


# %%
score_day(date.today())

# %%
