import pandas as pd
from matplotlib.pyplot import pie, axis, show
import argparse
import datetime

parser = argparse.ArgumentParser(description='Create a pie graphic representing the Slimcoin blocks rewards split by the kind of consensus used to produce each block.')

parser.add_argument('-s','--sum', action='store_true', help='sum rewards per block type')
parser.add_argument('beginning_date', metavar='beginning_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),
                    help='- the date to start from, format yyyy-mm-dd')
parser.add_argument('ending_date', metavar='ending_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),
                    help='- the date to end with, format yyyy-mm-dd')
args = parser.parse_args()

df = pd.read_csv ('https://github.com/slimcoin-project/slm-assets/raw/master/data.csv', index_col='date-time', parse_dates=True)
df = df.sort_index()
df= df.tz_convert (None)
df_after = df.loc[args.beginning_date : args.ending_date]

if args.sum:
    sums = df_after.groupby(df_after["consensus"])["mint"].sum()
else:
    counts=df_after["consensus"].value_counts()

axis('equal')

if args.sum:
    pie(sums, labels=sums.index)
else:
    pie(counts, labels=counts.index)

show()
