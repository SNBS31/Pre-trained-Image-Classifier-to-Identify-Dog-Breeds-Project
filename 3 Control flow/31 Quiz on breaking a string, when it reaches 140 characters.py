headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = "" # Since they said just a string, and not a list of strings. Hence, the indexing is starting from 0(seen in arrays)
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140: # Meaning it will end but at 139, from our knowledge of arrays
        news_ticker = news_ticker[:140]
        break
    
print(news_ticker)    