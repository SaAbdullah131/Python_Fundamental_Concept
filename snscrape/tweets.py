import snscrape.modules.twitter as snstwitter;
import pandas as pd;


query = "python";
tweets = [];
limit = 200;

for tweet in snstwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))
    break