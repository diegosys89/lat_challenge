from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets_data = pd.read_json(file_path, lines = "records")

    #Get top 10 dates
    tweets_data = tweets_data[["date","user","id"]]
    tweets_data["date"] = tweets_data["date"].dt.date
    tweets_data["user"] = tweets_data["user"].str.get("username")
    tweets_data.head()

    #top 10 days
    top_10_days = tweets_data.groupby(["date"]).count()
    top_10_days = top_10_days.sort_values("id", ascending=False).head(10)
    top_10_days = list(top_10_days.index)
    
    #filter data and group by date and user
    tweets_data = tweets_data.loc[tweets_data["date"].isin(top_10_days)]
    tweets_data = tweets_data.groupby(["date","user"]).count()

    tweets_data = tweets_data.sort_values(["date","id"], ascending=False)
    tweets_data = tweets_data.reset_index().groupby("date").first()
    
    tweets_data = [tuple(i) for i in tweets_data[["user"]].itertuples()]
    return tweets_data
