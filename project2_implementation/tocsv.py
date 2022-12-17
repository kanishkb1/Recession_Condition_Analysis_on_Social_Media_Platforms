import pandas as pd
from sqlalchemy import create_engine

db_connection_str = 'mysql+pymysql://root:admin123456@localhost'
db_connection = create_engine(db_connection_str)

query = 'select * from dsp_nyt.nyt'
df = pd.read_sql(query, con=db_connection)
df.to_csv (r'nyt.csv', index = False)
print('nyt.csv export successfull')

query = 'select * from dsp_reddit.reddit'
df = pd.read_sql(query, con=db_connection)
df.to_csv (r'reddit.csv', index = False)
print('reddit.csv export successfull')
        
query = 'select * from dsp_reddit.reddit_politics'
df = pd.read_sql(query, con=db_connection)
df.to_csv (r'reddit_politics.csv', index = False)
print('reddit_politics.csv export successfull')

query = 'select * from dsp_tweets.twitter'
df = pd.read_sql(query, con=db_connection)
df.to_csv (r'twitter.csv', index = False)
print('twitter.csv export successfull')
