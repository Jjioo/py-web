
def scrape_news():
    import requests
    import pymongo
    from bs4 import BeautifulSoup
    from pymongo import MongoClient
    import datetime
    import json,re
        # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["foxnews"]
    articles_collection = db["articles"]

    url = 'https://techcrunch.com/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    # Get article titles
    titles = soup.find_all('a',class_="post-block__title__link")
    title_list = [link.text.strip() for link in titles]

    writer = soup.find_all('span',class_="river-byline__authors")
    writer_list= [link.text.strip() for link in writer]
    

    # Save data to MongoDB
    articles_collection.insert_one({"titles": title_list,"writer":writer_list})

    # Save data to JSON file
    with open('foxnews_data.json', 'w') as f:
        json.dump({"titles": title_list, "writer":writer_list}, f)



