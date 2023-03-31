from flask import Flask, request, jsonify, render_template, redirect
import requests,json
from scrape_news import scrape_news
import os
import csv
from pymongo import MongoClient



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["news_articles"]
collection = db["articles"]

with open('foxnews_data.json', 'r') as f:
    data = json.load(f)

def get_stock_data(symbol):
    api_key = 'pk_05bfc04bdd7f4bcabb59c4cd87777aaa'
    url = f'https://cloud.iexapis.com/stable/stock/{symbol}/chart/1m?token={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return data

def read_csv_file(file_path):
    articles = []
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            articles.append(row)
    return articles



@app.route('/')
def display_data():
    articles = collection.find()
    return render_template('base.html', articles=articles)


@app.route('/about')
def about():
    return render_template('done.html')





@app.route('/news')
def news():

    with open('foxnews_data.json') as f:
        data = json.load(f)
    return render_template('mytemplate.html', titles=data['titles'], writer=data['writer'])







if __name__ == '__main__':
    print("Scraping news...")
    scrape_news()
    app.run(debug=True)
